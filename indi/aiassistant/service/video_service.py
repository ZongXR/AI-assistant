# -*- coding: utf-8 -*-
import os
import sys
from threading import Lock
import platform
import numpy as np
import cv2
from cv2 import CascadeClassifier
from flask import current_app
from indi.aiassistant.utils.img_utils import convert_img_to_tf
if platform.machine() in ("armv6l", "armv7l", "aarch64", "arm64"):
    from tflite_runtime.interpreter import Interpreter
else:
    from tensorflow.lite.python.interpreter import Interpreter


enable_server_camera = True
face_detector = CascadeClassifier(os.path.join(os.path.dirname(sys.argv[0]), "models", "haarcascade_frontalface_default.xml"))
face_detector_lock = Lock()

facenet = Interpreter(os.path.join(os.path.dirname(sys.argv[0]), "models", "facenet.tflite"), num_threads=4)
facenet.allocate_tensors()
facenet_lock = Lock()


def jpg_from_camera() -> bytes:
    vid = cv2.VideoCapture(current_app.config.get("CAMERA_ADDRESS"))
    while enable_server_camera:
        success, frame = vid.read()
        if success:
            image = cv2.imencode('.jpg', process_img(frame))[1].tobytes()
            yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + image + b'\r\n'


def process_img(frame: np.ndarray) -> np.ndarray:
    """
    处理捕获的图像并输出\n
    :param frame: 捕获的图像
    :return: 输出的图像
    """
    result = cv2.flip(frame, 1)
    # 人脸检测
    faces = detect_faces(result)
    faces_array = list()
    for x, y, w, h in faces:
        cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
        faces_array.append(convert_img_to_tf(frame[y:y + h, x:x + w].astype(np.float32), tuple(facenet.get_input_details()[0]["shape"][1:-1].tolist())))
    # TODO too slow to optimize
    # if len(faces_array) > 0:
    #     embedding = encode_face(np.stack(faces_array, axis=0))
    return result


def detect_faces(frame: np.ndarray) -> np.ndarray:
    """
    人脸检测\n
    :param frame: 输入图像
    :return: [(x, y, w, h), (x, y, w, h)]
    """
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    with face_detector_lock:
        return face_detector.detectMultiScale(gray_img, scaleFactor=1.15, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)


def encode_face(face: np.ndarray) -> np.ndarray:
    """
    人脸编码\n
    :param face: 人脸, OpenCV的BGR格式
    :return: 嵌入
    """
    with facenet_lock:
        facenet.set_tensor(facenet.get_input_details()[0]["index"], face)
        facenet.invoke()
        return facenet.get_tensor(facenet.get_output_details()[0]["index"])
