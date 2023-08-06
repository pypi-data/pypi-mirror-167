import dataclasses
from typing import Optional


@dataclasses.dataclass
class Keypoint:
    x: float
    y: float
    name: Optional[str]
    confidence: Optional[float]


class Keypoints(list):
    skeleton = [[]]

    def __getitem__(self, item) -> Keypoint:
        return super().__getitem__(item)
