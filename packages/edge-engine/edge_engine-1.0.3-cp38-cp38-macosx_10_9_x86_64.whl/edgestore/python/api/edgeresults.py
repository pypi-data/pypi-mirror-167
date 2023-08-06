from edgestore.protos.inference_api.primitivies.generic_detection_pb2 import GenericDetection
from edgestore.protos.inference_api.primitivies.point_pb2 import Point
from edgestore.protos.inference_api.primitivies.results_pb2 import Results
from edgestore.python.api.keypoints import Keypoint,Keypoints
from edgestore.python.api.label import Label
from edgestore.python.api.location import Location
from edgestore.python.api.recognition import Recognition
from edgestore.python.api.recognitions import Recognitions


class EdgeResults:
    def __init__(self, c_results):
        self.c_results = c_results
        results_bytes = c_results.serialize_result()
        results_bytes = bytes(results_bytes)
        self._results_proto = Results()
        self._results_proto.ParseFromString(results_bytes)

    @property
    def recognitions(self):
        _recognitions = Recognitions()
        for detection in self._results_proto.detections.detection:
            detection: GenericDetection
            keypoints = None

            if detection.points is not None:
                keypoints = Keypoints()
                for point in detection.points.point:
                    point:Point
                    keypoints.append(Keypoint(
                        x=point.data[0],
                        y=point.data[1],
                        confidence=point.pointClass.confidence,
                        name=point.pointClass.name
                    ))

            _recognitions.append(
            Recognition(
                label=Label(
                    class_id=detection.detectionClass.classID,
                    name=detection.detectionClass.name,
                    confidence=detection.detectionClass.confidence,
                ),
                location=Location(x_min=detection.box.minPoint.data[0],
                                  x_max=detection.box.maxPoint.data[0],
                                  y_min=detection.box.minPoint.data[1],
                                  y_max=detection.box.maxPoint.data[1]),
                color=detection.color,
                keypoints=keypoints




            ))

        return _recognitions

    def draw(self,image):
        return self.c_results.draw(image)