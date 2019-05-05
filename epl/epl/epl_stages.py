from surround import Stage, SurroundData
from sklearn.preprocessing import normalize
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

    def __init__(self):
        self.processed_data = pd.DataFrame()

    # This function clean the row containing empty field.
    def clean_empty_data(self):
        self.processed_data.dropna(inplace=True)

    # This function assign the rank of each team.
    def categorical_team_to_ordinal_value(self, team):
        elite_team = ["""'Man United'""", 'Liverpool', 'Arsenal', 'Chelsea', 'Tottenham']
        semi_elite_team = ["""'Man City'""", 'Everton', """'Aston Villa'""", 'Newcastle', 'Wolves']
        pro_team = ["""'Nottingham Forest'""", 'Blackburn', """'Sheffield Wednesday'""", 'Sunderland',
                    """'Leeds United'"""]
        semi_pro_team = ["""'West Brom'""", """'West Ham'""", """'Sheffield United'""", 'Leicester', 'Portsmouth']

        if team in elite_team:
            return 5
        elif team in semi_elite_team:
            return 4
        elif team in pro_team:
            return 3
        elif team in semi_pro_team:
            return 2
        else:
            return 1

    # This function normalizes the features on the columns_to_standardize.
    def normalize_data(self):
        columns_to_standardize = [['HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HR', 'AR']]

        for each_col in columns_to_standardize:
            self.processed_data[each_col] = normalize(self.processed_data[each_col])

    # This function shift column from middle to the last of the dataframe.
    def shift_column(self):
        temp_store = self.processed_data.pop('FTR')
        self.processed_data['FTR'] = temp_store

    def operate(self, surround_data, config):
        # Remove the row with the missing value of any attributes
        self.processed_data = surround_data.input_data
        self.clean_empty_data()
        print(self.processed_data.shape)
        print(self.processed_data.head(10))

        # Change the categorical ordinal data into Numerical value.
        self.processed_data['HomeTeam'] = self.processed_data['HomeTeam'].apply(
            self.categorical_team_to_ordinal_value)
        self.processed_data['AwayTeam'] = self.processed_data['AwayTeam'].apply(
            self.categorical_team_to_ordinal_value)

        print(self.processed_data.head(10))

        # Standardize the data using the pandas function
        self.normalize_data()
        print(self.processed_data.head(10))

        # Shift the FTR column to the last column.
        self.shift_column()
        print(self.processed_data.head(10))

        # Set the processed data to the SurroundData object
        surround_data.input_data = self.processed_data


class ModellingData(Stage):
    def operate(self, surround_data, config):
        print("This function is to be completed")
        surround_data.output_data = "TODO: Data Training, Testing and Predicting here"


class DataOutput(Stage):
    def operate(self, surround_data, config):
        surround_data.output_data = "TODO: Displaying the result here"
