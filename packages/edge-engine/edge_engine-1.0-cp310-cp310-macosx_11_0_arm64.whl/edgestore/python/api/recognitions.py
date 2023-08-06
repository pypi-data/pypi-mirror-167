from typing import List

import cv2
import numpy as np

from .recognition import Recognition
from collections import UserList


class Recognitions(UserList):
    def __getitem__(self, item) -> Recognition:
        return super().__getitem__(item)

    def applying(self, tr):
        return Recognitions([i.applying(tr) for i in self])

    def visualize(
        self, img: np.ndarray = None, confidence_threshold=0.5, color=None
    ):
        if img is not None:
            img = img.copy()
            num_detections = len(self)
            if num_detections > 0:
                # colors = sns.color_palette("husl", num_detections)
                recog: Recognition = self[0]

                if recog.segmentation_mask is not None:
                    segmentation = np.zeros(
                        (
                            recog.segmentation_mask.shape[0],
                            recog.segmentation_mask.shape[1],
                            3,
                        ),
                        dtype=np.uint8,
                    )
                    for recognition in self:
                        recognition: Recognition
                        segmentation[recognition.segmentation_mask == 1] = (
                            np.array(recognition.color) * 255
                        )
                    img = cv2.addWeighted(img, 0.5, segmentation, 0.5, 0)

        for recognition in self:
            recognition: Recognition
            if (
                recognition.confidence is None
                or recognition.confidence >= confidence_threshold
            ):
                recog_color = color
                if color is None and recognition.color is not None:
                    recog_color = (
                        (np.array(recognition.color) * 255)
                        .astype(np.uint8)
                        .tolist()
                    )
                recognition.visualize(img, color=recog_color)
        return img
