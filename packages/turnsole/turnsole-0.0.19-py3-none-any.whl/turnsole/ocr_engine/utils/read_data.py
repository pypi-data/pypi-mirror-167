# -*- coding: utf-8 -*-
# @Author        : Lyu Kui
# @Email         : 9428.al@gmail.com
# @Create Date   : 2022-06-16 10:59:50
# @Last Modified : 2022-08-03 14:59:15
# @Description   : 

import cv2
import base64
import numpy as np
import tensorflow as tf


def base64_to_bgr(img64):
    """把 base64 转换成图片
        单通道的灰度图或四通道的透明图都将自动转换成三通道的 BGR 图
    
    Args:
        img64 (TYPE): Description
    
    Returns:
        TYPE: image is a 3-D uint8 Tensor of shape [height, width, channels] where channels is BGR
    """
    encoded_image = base64.b64decode(img64)
    img_array = np.frombuffer(encoded_image, np.uint8)
    image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return image

def bytes_to_bgr(buffer: bytes):
    """Read a byte stream as a OpenCV image
    
    Args:
        buffer (TYPE): bytes of a decoded image
    """
    img_array = np.frombuffer(buffer, np.uint8)
    image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    # image = tf.io.decode_image(buffer, channels=3)
    # image = np.array(image)[...,::-1]
    return image