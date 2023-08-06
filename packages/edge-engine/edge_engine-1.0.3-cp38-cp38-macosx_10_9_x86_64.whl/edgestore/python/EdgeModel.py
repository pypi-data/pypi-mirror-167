from . import wrapper
from edgestore.protos.inference_api.primitivies.results_pb2 import Results

from edgestore.python.api.edgeresults import EdgeResults


class EdgeModel:
    def __init__(self, model_path):

        self.model = wrapper.EdgeModelWrapper(model_path)



    def run(self, *args):
        results = self.model.run(args[0])
        return EdgeResults(c_results=results)
