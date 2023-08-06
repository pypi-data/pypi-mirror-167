import dataclasses
from typing import List
import cv2
import numpy as np

from .keypoints import Keypoints
from .label import Label
from .location import Location


@dataclasses.dataclass
class Recognition:
    location: Location = None
    color: List = None
    keypoints: Keypoints = None
    segmentation_mask: np.ndarray = None
    text: str = None,
    label:Label=None


    @property
    def confidence(self):
        return self.label.confidence

    @property
    def display_name(self):
        return self.label.name

    @property
    def class_id(self):
        return self.label.class_id



    @property
    def is_empty(self):

        for field in dataclasses.fields(Recognition):
            if getattr(self, field.name) is not None:
                return False
        return True

    def restore_pad_normalized(self, width, height):
        if self.location is not None:
            self.location[0], self.location[1] = restore_from_pad_normalized(
                width, height, self.location[0], self.location[1]
            )
            self.location[2], self.location[3] = restore_from_pad_normalized(
                width, height, self.location[2], self.location[3]
            )
        if self.keypoints is not None:
            for i, kpt in enumerate(self.keypoints):
                (
                    self.keypoints[i][0],
                    self.keypoints[i][1],
                ) = restore_from_pad_normalized(width, height, kpt[0], kpt[1])

    def visualize(
        self,
        input_image: np.ndarray = None,
        thickness=None,
        keypoint_thresh=0.5,
        thickness_perc=0.5,
        color=None,
    ):
        if (
            self.location is not None
            or self.keypoints is not None
            or self.segmentation_mask is not None
        ):
            self.draw(
                input_image,
                thickness=thickness,
                keypoint_thresh=keypoint_thresh,
                thickness_perc=thickness_perc,
                color=color,
            )
        else:
            print(self)

    def applying(self, tr):
        # recog = deepcopy(self)
        self.apply_transform(tr)
        return self

    def apply_transform(self, tr: np.ndarray):

        tr = np.array(tr)
        assert tr.shape == (3, 3)
        if self.location is not None:
            loc = np.array(self.location)
            locr = loc.reshape((-1, 2))
            locr = np.concatenate((locr, np.ones((locr.shape[0], 1))), axis=1)
            locr = np.matmul(locr, tr.transpose())
            locr = locr[:, :2]
            self.location = locr.reshape(loc.shape)
        if self.keypoints is not None:
            kpts = np.array(self.keypoints)
            loc = kpts[:, :2]
            locr = np.concatenate((loc, np.ones((loc.shape[0], 1))), axis=1)
            locr = np.matmul(locr, tr.transpose())
            kpts[:, :2] = locr[:, :2]
            for i in range(len(self.keypoints)):
                self.keypoints[i] = kpts[i]

    def draw(
        self,
        img,
        thickness=None,
        keypoint_thresh=0.5,
        thickness_perc=0.5,
        color=None,
    ):
        self._draw(
            img,
            thickness=thickness,
            keypoint_thresh=keypoint_thresh,
            thickness_perc=thickness_perc,
            color=(80, 80, 180),
            draw_text=False,
        )
        self._draw(
            img,
            thickness=thickness,
            keypoint_thresh=keypoint_thresh,
            thickness_perc=thickness_perc * 0.8,
            color=color,
        )

    def _draw(
        self,
        img: np.ndarray,
        thickness=None,
        keypoint_thresh=0.5,
        thickness_perc=0.5,
        color=None,
        draw_text=True,
    ):
        h, w, _ = img.shape
        if thickness is None:
            dim = np.sqrt(h * w)
            thickness = int(dim * thickness_perc / 100)
            if thickness == 0:
                thickness = 1
        if self.location is not None:
            location = [int(i) for i in self.location.xyxy_list]
            pt1 = location[:2]
            pt2 = location[2:]

            if color is None:
                rect_color = random_color()
            else:
                rect_color = color

            cv2.rectangle(
                img,
                pt1=pt1,
                pt2=pt2,
                color=rect_color,
                thickness=thickness,
            )
            if self.display_name is not None:
                label = self.display_name.title()

                if self.confidence is not None:
                    confidence = int(self.confidence * 100)
                    label += f":{confidence}%"

                if draw_text:
                    ret, baseline = cv2.getTextSize(
                        label, cv2.FONT_HERSHEY_SIMPLEX, 2, thickness
                    )
                    text_w, text_h = ret
                    text_h += 10
                    box_w = location[2] - location[0]
                    mask = np.ones((text_h, text_w, 3), dtype=np.uint8) * 255
                    cv2.putText(
                        mask,
                        label,
                        (0, mask.shape[0] - 5),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        2,
                        (0, 0, 0),
                        thickness,
                    )
                    if mask.shape[1] > box_w:
                        scaling = box_w / mask.shape[1]
                        mask = cv2.resize(
                            mask, dsize=None, fx=scaling, fy=scaling
                        )
                        text_h, text_w, _ = mask.shape

                    xmin = int(location[0] + box_w / 2 - text_w / 2)
                    ymin = int(location[1])

                    xmin = clip(xmin, 0, w)
                    ymin = clip(ymin, 0, h)
                    ymax = ymin + text_h
                    xmax = xmin + text_w
                    xmax = clip(xmax, xmin, w)
                    ymax = clip(ymax, ymin, h)
                    if xmax - xmin != 0 and ymax - ymin != 0:
                        mask = cv2.resize(mask, (xmax - xmin, ymax - ymin))

                        original = img[ymin:ymax, xmin:xmax]
                        # mask = np.ones_like(original)*255

                        # img[ymin:ymax, xmin:xmax] = mask

                        cv2.addWeighted(
                            original,
                            0.5,
                            mask,
                            0.5,
                            0,
                            img[ymin:ymax, xmin:xmax],
                        )

                        # cv2.putText(img, label, (xmin, ymin), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), thickness)

        if self.keypoints is not None:
            if color is None:
                skl_color = (0, 0, 0)
            else:
                skl_color = color
            for idx in self.keypoints.skeleton:
                if len(idx) == 2:
                    start_idx, end_idx = idx
                    start_kpt = self.keypoints[start_idx]
                    end_kpt  = self.keypoints[end_idx]
                    x1, y1, confidence1 = start_kpt.x,start_kpt.y,start_kpt.confidence
                    x2, y2, confidence2 = end_kpt.x,end_kpt.y,end_kpt.confidence
                    if (
                        confidence1 > keypoint_thresh
                        and confidence2 > keypoint_thresh
                    ):
                        cv2.line(
                            img,
                            pt1=(int(x1), int(y1)),
                            pt2=(int(x2), int(y2)),
                            color=skl_color,
                            thickness=thickness,
                        )
            for keypoint in self.keypoints:
                if color is None:
                    kpt_color = random_color()
                else:
                    kpt_color = color
                x, y, confidence = keypoint.x,keypoint.y,keypoint.confidence
                if confidence > keypoint_thresh:
                    cv2.circle(
                        img,
                        (int(x), int(y)),
                        thickness * 2,
                        kpt_color,
                        cv2.FILLED,
                    )


def clip(val, lower_limit, upper_limit):
    if val < lower_limit:
        return lower_limit
    elif val > upper_limit:
        return upper_limit
    else:
        return val


def random_color():
    color = np.random.random(3) * 255
    return tuple(color.tolist())


def restore_from_pad_on_smaller_side(
    smaller_side_length, larger_side_length, normalized_pt
):
    ar = larger_side_length / smaller_side_length
    return (normalized_pt - 0.5) * ar + 0.5


def restore_from_pad_normalized(width: int, height: int, x, y):
    if width < height:
        xOut = restore_from_pad_on_smaller_side(
            smaller_side_length=width,
            larger_side_length=height,
            normalized_pt=x,
        )
        return xOut, y
    elif width > height:
        yOut = restore_from_pad_on_smaller_side(
            smaller_side_length=height,
            larger_side_length=width,
            normalized_pt=y,
        )
        return x, yOut
    else:
        return x, y
