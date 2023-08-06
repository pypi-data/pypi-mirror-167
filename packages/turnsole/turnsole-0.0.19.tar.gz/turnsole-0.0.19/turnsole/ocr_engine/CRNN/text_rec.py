import os
import io
import cv2
import time
import numpy as np
import turnsole.ocr_engine.CRNN.alphabets as alphabets
import tritonclient.grpc as grpcclient


def sort_poly(p):
    # Find the minimum coordinate using (Xi+Yi)
    min_axis = np.argmin(np.sum(p, axis=1))
    # Sort the box coordinates
    p = p[[min_axis, (min_axis + 1) % 4, (min_axis + 2) % 4, (min_axis + 3) % 4]]
    if abs(p[0, 0] - p[1, 0]) > abs(p[0, 1] - p[1, 1]):
        return p
    else:
        return p[[0, 3, 2, 1]]

def client_init(url="localhost:8001",
                ssl=False, private_key=None, root_certificates=None, certificate_chain=None,
                verbose=False):
    triton_client = grpcclient.InferenceServerClient(
        url=url,
        verbose=verbose,
        ssl=ssl,
        root_certificates=root_certificates,
        private_key=private_key,
        certificate_chain=certificate_chain)
    return triton_client

class textRecServer:
    def __init__(self):
        super().__init__()
        self.charactersS = ' ' + alphabets.alphabet
        self.batchsize = 8

        self.input_name = 'INPUT__0'
        self.output_name = 'OUTPUT__0'
        self.model_name = 'text_rec_half'
        self.np_type = np.float16
        self.quant_type = "FP16"

        # self.input_name = 'input' # 'INPUT__0'
        # self.output_name = 'output' # 'OUTPUT__0'
        # self.model_name = 'text_rec_trt' # 'text_rec_half'
        # self.np_type = np.float32
        # self.quant_type = "FP32"

        self.compression_algorithm = None
        self.outputs = []
        self.outputs.append(grpcclient.InferRequestedOutput(self.output_name))

    def preprocess_one_image(self, image):
        _, w, _ = image.shape
        image = self._transform(image, w)
        return image

    def predict_batch(self, im, boxes):
        """Summary
        
        Args:
            im (TYPE): RGB
            boxes (TYPE): Description
        
        Returns:
            TYPE: Description
        """

        triton_client = client_init("localhost:8001")
        count_boxes = len(boxes)
        boxes = sorted(boxes,
                       key=lambda box: int(32.0 * (np.linalg.norm(box[0] - box[1])) / (np.linalg.norm(box[3] - box[0]))),
                       reverse=True)
    
        results = {}
        labels = []
        rectime = 0.0
        if len(boxes) != 0:
            for i in range(len(boxes) // self.batchsize + int(len(boxes) % self.batchsize != 0)):
                box = boxes[min(len(boxes)-1, i * self.batchsize)]
                w, h = [int(np.linalg.norm(box[0] - box[1])), int(np.linalg.norm(box[3] - box[0]))]
                width = max(32, min(int(32.0 * w / h), 960))
                if width < 32:
                    continue
                slices = []
                for index, box in enumerate(boxes[i * self.batchsize:(i + 1) * self.batchsize]):
                    _box = [n for a in box for n in a]
                    if i * self.batchsize + index < count_boxes:
                        results[i * self.batchsize + index] = [list(map(int, _box))]
                    w, h = [int(np.linalg.norm(box[0] - box[1])), int(np.linalg.norm(box[3] - box[0]))]
                    pts1 = np.float32(box)
                    pts2 = np.float32([[0, 0], [w, 0], [w, h], [0, h]])

                    # 前处理优化
                    xmin, ymin, _w, _h = cv2.boundingRect(pts1)
                    xmax, ymax = xmin+_w, ymin+_h
                    xmin, ymin = max(0, xmin), max(0, ymin)
                    im_sclice = im[int(ymin):int(ymax), int(xmin):int(xmax), :]
                    pts1[:, 0] -= xmin
                    pts1[:, 1] -= ymin

                    M = cv2.getPerspectiveTransform(pts1, pts2)
                    im_crop = cv2.warpPerspective(im_sclice, M, (w, h))
                    im_crop = self._transform(im_crop, width)
                    slices.append(im_crop)
                start_rec = time.time()
                slices = self.np_type(slices)
                slices = slices.transpose(0, 3, 1, 2)
                slices = slices/127.5-1.
                inputs = []
                inputs.append(grpcclient.InferInput(self.input_name, list(slices.shape), self.quant_type))
                inputs[0].set_data_from_numpy(slices)

                # inference
                preds = triton_client.infer(
                    model_name=self.model_name,
                    inputs=inputs,
                    outputs=self.outputs,
                    compression_algorithm=self.compression_algorithm
                )
                preds = preds.as_numpy(self.output_name).copy()
                preds = preds.transpose(1, 0)
                tmp_labels = self.decode(preds)
                rectime += (time.time() - start_rec)
                labels.extend(tmp_labels)

            for index, label in enumerate(labels[:count_boxes]):
                label = label.replace(' ', '').replace('￥', '¥')
                if label == '':
                    del results[index]
                    continue
                results[index].append(label)
            # 重新排序
            results = list(results.values())
            results = sorted(results, key=lambda x: x[0][1], reverse=False) # 按 y0 从小到大排
            keys = [str(i) for i in range(len(results))]
            results = dict(zip(keys, results))
        else:
            results = dict()
            rectime = -1
        return results, rectime
        
    def decode(self, preds):
        res = []
        for t in preds:
            length = len(t)
            char_list = []
            for i in range(length):
                if t[i] != 0 and (not (i > 0 and t[i-1] == t[i])):
                    char_list.append(self.charactersS[t[i]])
            res.append(u''.join(char_list))
        return res

    def _transform(self, im, width):
        height=32

        ori_h, ori_w = im.shape[:2]
        ratio1 = width * 1.0 / ori_w
        ratio2 = height * 1.0 / ori_h
        if ratio1 < ratio2:
            ratio = ratio1
        else:
            ratio = ratio2
        new_w, new_h = int(ori_w * ratio), int(ori_h * ratio)
        if new_w<4:
            new_w = 4
        im = cv2.resize(im, (new_w, new_h))
        img = np.ones((height, width, 3), dtype=np.uint8)*230
        img[:im.shape[0], :im.shape[1], :] = im
        return img
