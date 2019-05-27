# Developed by Dipesh Bhatta
# dbhatta@deakin.edu.au

import logging
import pandas as pd
import glob
from surround import Config
from wrapper import PipelineWrapper

logging.basicConfig(level=logging.INFO)


def fetch_data(surround_config):
    dir_path = surround_config.get_path("surround.path_to_epl_data")
    all_files = glob.glob(dir_path + "/*.csv")

    df_from_each_file = (pd.read_csv(f) for f in all_files)
    input_data = pd.concat(df_from_each_file, ignore_index=True, sort=False)
    logging.info("Data loaded with the shape of... {0}" .format(input_data.shape))
    return input_data


def main():
    logging.basicConfig(level=logging.INFO)
    surround_config = Config()
    surround_config.read_config_files(["config.yaml"])
    # Fetch the data from the data folder.
    raw_data = fetch_data(surround_config)

    wrapper = PipelineWrapper(surround_config)
    wrapper.run(raw_data)


if __name__ == "__main__":
    main()