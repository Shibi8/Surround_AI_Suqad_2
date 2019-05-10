import logging
from surround import Surround, Config
from arima.SVR_stages import FeedData, SVRData, ComputeForecast
# from .wrapper import PipelineWrapper
# import os
# import json
logging.basicConfig(level=logging.INFO)


# def main():
#     wrapper = PipelineWrapper()
#     config = wrapper.get_config()
#     output = wrapper.run(json.dumps({"data": "hello"}))
#     with open(os.path.join(config["output_path"], "output.txt"), 'w') as f:
#         f.write(output["output"])
#     logging.info(output)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    surround = Surround([FeedData(), ComputeForecast()])
    surround_config = Config()
    surround_config.read_config_files(["config.yaml"])
    surround.set_config(surround_config)
    surround.init_stages()

    surround.process(SVRData(), ComputeForecast())