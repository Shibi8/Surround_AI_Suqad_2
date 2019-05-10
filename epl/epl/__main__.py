import logging
import pandas as pd
import glob
from surround import Surround, Config
from epl.epl.epl_stages import EplData, WranglingData, ModellingAndPrediction
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

def fetch_data(surround_config):
    dir_path = surround_config.get_path("surround.path_to_epl_data")
    all_files = glob.glob(dir_path + "/*.csv")

    df_from_each_file = (pd.read_csv(f) for f in all_files)
    input_data = pd.concat(df_from_each_file, ignore_index=True, sort=False)
    logging.info("Input data works.")
    logging.info(input_data.shape)
    logging.info("this is good")
    return input_data


def main():
    logging.basicConfig(level=logging.INFO)
    surround = Surround([WranglingData(), ModellingAndPrediction()])
    surround_config = Config()
    surround_config.read_config_files(["config.yaml"])
    surround.set_config(surround_config)
    surround.init_stages()

    # Fetch the data from the data folder.
    raw_data = fetch_data(surround_config)
    # epl_data is created as the SurroundData type.
    epl_data = EplData()
    # raw_data is fed into epl_data.
    epl_data.feed_data(raw_data)

    # Surround process started.
    surround.process(epl_data)


if __name__ == "__main__":
    main()