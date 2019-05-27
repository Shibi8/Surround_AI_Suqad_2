from surround import Surround, Wrapper, AllowedTypes
from epl_stages import EplData, WranglingData, ModellingAndPrediction, DisplayOutput


class PipelineWrapper(Wrapper):
    def __init__(self, surround_config):
        surround = Surround([WranglingData(), ModellingAndPrediction(), DisplayOutput()], __name__)
        surround.set_config(surround_config)
        super().__init__(surround)

    def run(self, input_data):
        # epl_data is created as the SurroundData type.
        epl_data = EplData()
        # raw_data is fed into epl_data.
        epl_data.feed_data(input_data)

        # Surround process started.
        self.surround.process(epl_data)