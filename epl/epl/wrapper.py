import os
import json
from surround import Surround, Wrapper, AllowedTypes
from .epl_stages import EplData, DataInput


class PipelineWrapper(Wrapper):
    def __init__(self):
        surround = Surround([DataInput()], __name__)
        super().__init__(surround)

    # def run(self, input_data):
    #     text = json.loads(input_data)["data"]
    #     data = EplData(text)
    #     self.surround.process(data)
    #     return {"output": data.output_data}
