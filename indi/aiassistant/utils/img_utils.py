# -*- coding: utf-8 -*-
import numpy as np
import cv2


def convert_img_to_tf(img: np.ndarray, target_size: tuple) -> np.ndarray:
    """
    把一张图片转换成能够输入神经网络的形式\n
    :param img: 一张图片
    :param target_size: 大小
    :return: 新的图片
    """
    result = cv2.resize(img, target_size, interpolation=cv2.INTER_AREA)
    return cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
