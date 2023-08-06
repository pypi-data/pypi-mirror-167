import dataclasses

import numpy as np
import cv2


@dataclasses.dataclass
class SegmentationResults:
    raw_mask: np.ndarray

    def mask(self, width, height):
        return cv2.resize(self.raw_mask, (width, height))

    def overlay_on_image(self, image):
        height = image.shape[0]
        width = image.shape[1]
        mask = self.mask(width, height)
        return cv2.addWeighted(image, 0.5, mask, 0.5, 0)
