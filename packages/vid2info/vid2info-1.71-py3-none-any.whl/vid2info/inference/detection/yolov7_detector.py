"""
This class implements the YoloDetector. It is used to detect elements in a
given image or batch of images. It uses YOLOv6 as the backbone of the detector.

Author: Eric Canas.
Github: https://github.com/Eric-Canas
Email: eric@ericcanas.com
Date: 09-07-2022
"""

from vid2info.inference.detection.__yolo_detector import __YoloDetector

from vid2info.inference.detection.config import WEIGTHS_PATH, DETECTOR_MIN_CONFIDENCE_TH, IOU_NMS_TH, \
    MAX_DETECTIONS_PER_IMAGE, DETECTOR_IMAGE_SIZE, HALF_MODE, DATASET_YML
from vid2info.inference.config import INFERENCE_DEVICE

from yolov7.utils.torch_utils import TracedModel
from torch.backends import cudnn
import os
import torch


class YoloV7Detector(__YoloDetector):
    def __init__(self, weights : str = WEIGTHS_PATH, dataset_yml : str | None = DATASET_YML,
                 confidence_th : float = DETECTOR_MIN_CONFIDENCE_TH, nms_th : float = IOU_NMS_TH,
                 max_dets : int = MAX_DETECTIONS_PER_IMAGE, inference_device : str = INFERENCE_DEVICE,
                 image_size : int = DETECTOR_IMAGE_SIZE, half_mode = HALF_MODE,
                 merge_batches: bool = False, agnostic_nms: bool = False, trace: bool =True):

        """
        Initialize the YoloDetector (YoloV6).

        :param weights: String. Path to the weights file. It must be the .pt file generated by the YOLOv6 tool.
        :param dataset_yml: String. Path to the dataset .yaml file used for training the model in the YOLOv6 tool. It
                            must contain the 'nc' and 'names' fields.
        :param confidence_th: Float. The confidence threshold to use for assuming that a detection is valid. Take
                                into account that, when the detector is used within the pipeline together with the tracker,
                                this threshold will be used only for filtering high confidence detections with non-max
                                suppression, but it will also internally return everything below it. (To let the tracker
                                make its magic).
        :param nms_th: Float. The IoU threshold to use for non-max suppression.
        :param max_dets: Integer (greater than 0). The maximum number of detections to return by frame.
        :param inference_device: String ('cpu', 'cuda' or 'cuda:[int]'). The device to use for inference.
        :param image_size: Integer. The size of the images to use for inference.
        :param half_mode: Boolean. Whether to use half precision or not. Half precision only works with CUDA.
        :param merge_batches: Boolean. Whether to merge batches or not. If it is True, and the input is a batch
                                of images, predictions will be merged as if they came from a single image. It is only
                                recommended for very static scenes.
        :param agnostic_nms: Boolean. Whether to use agnostic nms or not. If it is True, the detector will use the
                                agnostic nms algorithm.
        """
        assert os.path.isfile(weights), f'Weights file {weights} not found.'
        super().__init__(confidence_th=confidence_th, nms_th=nms_th, max_dets=max_dets, dataset_yml=dataset_yml,
                         inference_device=inference_device, image_size=image_size, half_mode=half_mode,
                         merge_batches=merge_batches, agnostic_nms=agnostic_nms)
        self.model = torch.load(weights, map_location=self.inference_device)  # load
        self.model = self.model['ema' if self.model.get('ema') else 'model'].float().fuse().eval()
        cudnn.benchmark = True
        self.prepare_model()
        if trace:
            self.model = TracedModel(self.model, self.inference_device, self.image_size)

    def _predict(self, image: torch.Tensor) -> torch.Tensor:
        """
        Predict the detections in a given image.

        :param image: torch.Tensor. The image to predict the detections in.
        :return: torch.Tensor. The detections in the image.
        """
        assert self.model is not None, 'The YOLOv7 model has not been initialized.'
        assert not image.requires_grad, 'The image should not require gradients for inference.'
        return self.model(image, augment=True)[0]