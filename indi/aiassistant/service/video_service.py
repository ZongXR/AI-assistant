# -*- coding: utf-8 -*-
import numpy as np
import cv2
from cv2 import CascadeClassifier
from flask import current_app


enable_server_camera = True
face_detector = CascadeClassifier("./models/haarcascade_frontalface_default.xml")


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
    for x, y, w, h in faces:
        cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
    return result


def detect_faces(frame: np.ndarray) -> np.ndarray:
    """
    人脸检测\n
    :param frame: 输入图像
    :return: [(x, y, w, h), (x, y, w, h)]
    """
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = face_detector.detectMultiScale(gray_img, scaleFactor=1.15, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
    return result
