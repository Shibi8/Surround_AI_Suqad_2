import json
from surround import Surround, Wrapper, AllowedTypes
from Stages import ValidateData, SVRData

class PipelineWrapper(Wrapper):
    def __init__(self):
        surround = Surround([ValidateData()], __name__)
        super().__init__(surround)

    def run(self, input_data):
        text = json.loads(input_data)["data"]
        data = SVRData(text)
        self.surround.process(data)
        return {"output": data.output_data}
