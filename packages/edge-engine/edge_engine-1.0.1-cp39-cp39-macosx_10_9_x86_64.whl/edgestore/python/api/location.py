from dataclasses import dataclass

import numpy as np


@dataclass
class Location:
    x_min: float
    y_min: float
    x_max: float
    y_max: float

    @property
    def xyxy_list(self):
        return [self.x_min, self.y_min, self.x_max, self.y_max]

    @property
    def xyxy_array(self):
        return np.array(self.xyxy_list)
