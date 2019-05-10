from surround import Stage, SurroundData
from sklearn.preprocessing import normalize
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

import time
import glob
import logging


class EplData(SurroundData):

    def __init__(self):
        self.input_data = pd.DataFrame()
        self.errors = []

    def feed_data(self, surround_data):
        self.input_data = surround_data

# Task of this class is done in fetch_data() function in main file.
# class DataInput(Stage):
#
#     def __init__(self):
#         self.input_data = pd.DataFrame()
#
#     def init_stage(self, config):
#         dir_path = config.get_path("surround.path_to_epl_data")
#         all_files = glob.glob(dir_path + "/*.csv")
#
#         df_from_each_file = (pd.read_csv(f) for f in all_files)
#         self.input_data = pd.concat(df_from_each_file, ignore_index=True, sort=False)
#         logging.info("Input data works.")
#         logging.info(self.input_data.shape)
#         logging.info("this is good")
#         # self.input_data = all_files
#
#     def operate(self, surround_data, config):
#         logging.info("Data assignment started...")
#         surround_data.feed_data(self.input_data)
#         print(surround_data.input_data.shape)
#         logging.info("Data assignment completed.")


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

    # This function normalizes the features on the columns_to_normalize.
    def normalize_data(self):
        columns_to_standardize = [['HomeTeam', 'AwayTeam', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HR', 'AR']]

        for each_col in columns_to_standardize:
            self.processed_data[each_col] = normalize(self.processed_data[each_col])

    # This function shift column from middle to the last of the dataframe.
    def shift_column(self):
        temp_store = self.processed_data.pop('FTR')
        self.processed_data['FTR'] = temp_store

    # # This function plot the histogram of given column
    # def plot_histogram(self):
    #     histo_input = input("Do you want to print Histogram of any columns? y:n")
    #     while histo_input == "y":
    #         print("These are the column lists:", self.processed_data.head(1), "/n")
    #         column_input = input("Select one column:")
    #         plt.hist(self.processed_data[column_input])
    #         plt.show()
    #         histo_input = input("Do you want to print Histogram of any columns again? y:n")

    def operate(self, surround_data, config):
        # Remove the row with the missing value of any attributes
        self.processed_data = surround_data.input_data
        self.clean_empty_data()
        print(self.processed_data.shape)
        print(self.processed_data.head(10))

        # Delete two column with extra information (Total goal scored by the team)
        self.processed_data.pop('FTAG')
        self.processed_data.pop('FTHG')

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

        # # Plot the histogram of certain column.
        # self.plot_histogram()
        print(self.processed_data.head(10))

        # Set the processed data to the SurroundData object
        surround_data.input_data = self.processed_data


class ModellingAndPrediction(Stage):

    def __init__(self):
        self.processed_data = pd.DataFrame()

    def prediction_report(self, real, prediction):
        h = 0
        a = 0
        d = 0
        for x in prediction:
            if x == "H":
                h = h + 1
            elif x == "A":
                a = a + 1
            else:
                d = d + 1
        print("Total home win: {0}".format(h))
        print("Total away win: {0}".format(a))
        print("Total draw: {0}".format(d))

        # This is the confusion matrix of Home win, Away win or Draw.
        labels = ["A", "D", "H"]
        cnf_matrix = metrics.confusion_matrix(real, prediction, labels)
        print(cnf_matrix)

        print("The accuracy of the Logistic regression model is: {0}" .format(metrics.accuracy_score(real, prediction)))

    # Function to create the training and test data
    def train_test_data(self):
        feature_columns = ['HomeTeam', 'AwayTeam', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HR', 'AR']

        x_data = self.processed_data[feature_columns]
        y_data = self.processed_data['FTR']
        print(x_data)
        print(y_data)

        x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3, random_state=55)

        # instantiate the model (using the default parameters)
        log_reg = LogisticRegression()

        # fit the model with data
        log_reg.fit(x_train, y_train)

        # This is the predicted data.
        y_predicted = log_reg.predict(x_test)
        print("This is the predicted data {0}".format(y_predicted))

        # Prediction statistics
        self.prediction_report(y_test, y_predicted)

    def operate(self, surround_data, config):
        self.processed_data = surround_data.input_data
        print("This function is to be completed")
        self.train_test_data()


class DataOutput(Stage):
    def operate(self, surround_data, config):
        surround_data.output_data = "TODO: Displaying the result here"
