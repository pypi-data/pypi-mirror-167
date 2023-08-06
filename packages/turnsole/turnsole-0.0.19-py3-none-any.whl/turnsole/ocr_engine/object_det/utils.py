import grpc
import turnsole
import numpy as np
import tensorflow as tf
from tensorflow_serving.apis import predict_pb2, prediction_service_pb2_grpc


class ObjectDetection():

    """通用文件检测算法
    输入图片输出检测结果

    API 文档请参阅：
    """

    def __init__(self, confidence_threshold=0.5):
        """初始化检测对象

        Args:
            confidence_threshold (float, optional): 目标检测模型的分类置信度
        """

        self.lable2index = {
            'id_card_info':           0,
            'id_card_guohui':         1,
            'lssfz_front':            2,
            'lssfz_back':             3,
            'jzz_front':              4,
            'jzz_back':               5,
            'txz_front':              6,
            'txz_back':               7,
            'bank_card':              8,
            'vehicle_license_front':  9,
            'vehicle_license_back':  10,
            'driving_license_front': 11,
            'driving_license_back':  12,
            'vrc_page_12':           13,
            'vrc_page_34':           14,
        }
        self.index2lable = list(self.lable2index.keys())

    # def resize_and_pad_to_384(self, image, jitter=True):
    #     """长边在 256-384 之间随机取一个数，四边 pad 到 384

    #     Args:
    #         image (TYPE): An image represented as a numpy ndarray.
    #     """
    #     image_shape = tf.cast(tf.shape(image)[:2], dtype=tf.float32)
    #     max_side = tf.random.uniform(
    #         (), 256, 384, dtype=tf.float32) if jitter else 384.
    #     ratio = max_side / tf.reduce_max(image_shape)
    #     image_shape = tf.cast(ratio * image_shape, dtype=tf.int32)
    #     image = tf.image.resize(image, image_shape)
    #     image = tf.image.pad_to_bounding_box(image, 0, 0, 384, 384)
    #     return image, ratio

    def process(self, image):
        """Processes an image and returns a list of the detected object location and classes data.

        Args:
            image (TYPE): An image represented as a numpy ndarray.
        """
        h, w, _ = image.shape
        # image, ratio = self.resize_and_pad_to_384(image, jitter=False)
        image, ratio = turnsole.resize_with_pad(image, target_height=384, target_width=384)
        inputs = np.expand_dims(image/255., axis=0)

        options = [('grpc.max_send_message_length', 1000 * 1024 * 1024),
                   ('grpc.max_receive_message_length', 1000 * 1024 * 1024)]
        channel = grpc.insecure_channel('localhost:8500', options=options)
        stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

        request = predict_pb2.PredictRequest()
        request.model_spec.name = 'object_detection'
        request.model_spec.signature_name = 'serving_default'
        request.inputs['image'].CopyFrom(tf.make_tensor_proto(inputs, dtype='float32'))
        # 100 secs timeout
        result = stub.Predict(request, 100.0)

        # saved_model_cli show --dir saved_model/ --all                                         # 查看 saved model 的输入输出
        boxes = tf.make_ndarray(result.outputs['decode_predictions'])
        scores = tf.make_ndarray(result.outputs['decode_predictions_1'])
        classes = tf.make_ndarray(result.outputs['decode_predictions_2'])
        valid_detections = tf.make_ndarray(
            result.outputs['decode_predictions_3'])

        boxes = boxes[0][:valid_detections[0]]
        scores = scores[0][:valid_detections[0]]
        classes = classes[0][:valid_detections[0]]

        object_list = []
        for box, score, class_index in zip(boxes, scores, classes):
            xmin, ymin, xmax, ymax = box / ratio
            xmin = max(0, int(xmin))
            ymin = max(0, int(ymin))
            xmax = min(w, int(xmax))
            ymax = min(h, int(ymax))
            class_label = self.index2lable[int(class_index)]
            item = {
                "label": class_label,
                "confidence": float(score),
                "location": {
                    "xmin": xmin,
                    "ymin": ymin,
                    "xmax": xmax,
                    "ymax": ymax
                }
            }
            object_list.append(item)

        return object_list