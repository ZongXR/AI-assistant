# -*- coding: utf-8 -*-
import cv2


enable_server_camera = True


def jpg_from_camera() -> bytes:
    vid = cv2.VideoCapture(0)
    while enable_server_camera:
        success, frame = vid.read()
        if success:
            image = cv2.imencode('.jpg', cv2.flip(frame, 1))[1].tobytes()
            yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + image + b'\r\n'
