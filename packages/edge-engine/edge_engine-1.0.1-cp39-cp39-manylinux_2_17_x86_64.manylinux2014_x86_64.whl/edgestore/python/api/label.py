import dataclasses
from typing import Optional


@dataclasses.dataclass
class Label:
    name: Optional[str]
    class_id:Optional[int]
    confidence: Optional[float]
