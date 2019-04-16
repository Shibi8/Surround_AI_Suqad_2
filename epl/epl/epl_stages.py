from surround import Stage, SurroundData
import pandas as pd
import glob
import logging


class EplData(SurroundData):

    def __init__(self):
        self.input_data = pd.DataFrame()
        self.errors = []

    def feed_data(self, surround_data):
        self.input_data = surround_data


class DataInput(Stage):

    def __init__(self):
        self.input_data = pd.DataFrame()

    def init_stage(self, config):
        dir_path = config.get_path("surround.path_to_epl_data")
        all_files = glob.glob(dir_path + "/*.csv")

        df_from_each_file = (pd.read_csv(f) for f in all_files)
        self.input_data = pd.concat(df_from_each_file, ignore_index=True, sort=False)
        logging.info("Input data works.")
        logging.info(self.input_data.shape)
        logging.info("this is good")
        # self.input_data = all_files

    def operate(self, surround_data, config):
        logging.info("Data assignment started...")
        surround_data.feed_data(self.input_data)
        print(surround_data.input_data.shape)
        logging.info("Data assignment completed.")


class WranglingData(Stage):
    def operate(self, surround_data, config):
        surround_data.output_data = "TODO: Clean data here"


class ModellingData(Stage):
    def operate(self, surround_data, config):
        surround_data.output_data = "TODO: Data Training, Testing and Predicting here"


class DataOutput(Stage):
    def operate(self, surround_data, config):
        surround_data.output_data = "TODO: Displaying the result here"
