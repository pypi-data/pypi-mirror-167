# -*- coding: utf-8 -*-
# @Author        : lk
# @Email         : 9428.al@gmail.com
# @Create Date   : 2022-02-08 14:10:00
# @Last Modified : 2022-09-06 14:45:10
# @Description   : 

import turnsole
import numpy as np
import tensorflow as tf

import grpc
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc


# def resize_and_pad_to_1024(image, jitter=True):
#     # 长边在 512-1024 之间随机取一个数，四边 pad 到 1024
#     image_shape = tf.cast(tf.shape(image)[:2], dtype=tf.float32)
#     max_side = tf.random.uniform((), 512, 1024, dtype=tf.float32) if jitter else 1024.
#     ratio = max_side / tf.reduce_max(image_shape)
#     image_shape = tf.cast(ratio * image_shape, dtype=tf.int32)
#     image = tf.image.resize(image, image_shape)
#     image = tf.image.pad_to_bounding_box(image, 0, 0, 1024, 1024)
#     return image, ratio

class SignatureDetection():

    """签字盖章检测算法
    输入图片输出检测结果

    API 文档请参阅：
    """

    def __init__(self, confidence_threshold=0.5):
        """初始化检测对象
        
        Args:
            confidence_threshold (float, optional): 目标检测模型的分类置信度
        """

        self.lable2index = {
                'circle':    0,
                'ellipse':   1,
                'rectangle': 2,
                'signature': 3,
                'qr_code':   4,
                'bar_code':  5
            }
        self.index2lable = {
                0: 'circle',
                1: 'ellipse',
                2: 'rectangle',
                3: 'signature',
                4: 'qr_code',
                5: 'bar_code'
            }


    def process(self, image):
        """Processes an image and returns a list of the detected signature location and classes data.
        
        Args:
            image (TYPE): An image represented as a numpy ndarray.
        """
        h, w, _ = image.shape

        # image, ratio = resize_and_pad_to_1024(image, jitter=False)
        image, ratio = turnsole.resize_with_pad(image, target_height=1024, target_width=1024)
        inputs = np.expand_dims(np.float32(image/255.), axis=0)

        options = [('grpc.max_send_message_length', 1000 * 1024 * 1024),
                   ('grpc.max_receive_message_length', 1000 * 1024 * 1024)]
        channel = grpc.insecure_channel('localhost:8500', options=options)
        stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

        request = predict_pb2.PredictRequest()
        request.model_spec.name = 'signature_model'
        request.model_spec.signature_name = 'serving_default'
        request.inputs['image'].CopyFrom(tf.make_tensor_proto(inputs, dtype='float32'))
        result = stub.Predict(request, 100.0)                                                   # 100 secs timeout

        # saved_model_cli show --dir saved_model/ --all         # 查看 saved model 的输入输出
        boxes = tf.make_ndarray(result.outputs['decode_predictions'])
        scores = tf.make_ndarray(result.outputs['decode_predictions_1'])
        classes = tf.make_ndarray(result.outputs['decode_predictions_2'])
        valid_detections = tf.make_ndarray(result.outputs['decode_predictions_3'])
        
        boxes = boxes[0][:valid_detections[0]]
        scores = scores[0][:valid_detections[0]]
        classes = classes[0][:valid_detections[0]]

        signature_list = []
        for box, score, class_index in zip(boxes, scores, classes):
            xmin, ymin, xmax, ymax = box / ratio
            class_label = self.index2lable[class_index]
            item = {
                "label": class_label,
                "confidence": float(score),
                "location": {
                    "xmin": max(0, int(xmin)),
                    "ymin": max(0, int(ymin)),
                    "xmax": min(w, int(xmax)),
                    "ymax": min(h, int(ymax))
                }
            }
            signature_list.append(item)

        return signature_list
