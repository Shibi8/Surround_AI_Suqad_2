from surround import Stage, SurroundData

class EplData(SurroundData):
    output_data = None

    def __init__(self, input_data):
        self.input_data = input_data
        self.errors = []

class ValidateData(Stage):
    def operate(self, surround_data, config):
        surround_data.output_data = "TODO: Validate input data assumptions here"
