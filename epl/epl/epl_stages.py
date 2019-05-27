# Developed by Dipesh Bhatta
# dbhatta@deakin.edu.au
from surround import Stage, SurroundData
from sklearn.preprocessing import normalize
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from dbhatta_algorithm import DbhattaAlgorithm


class EplData(SurroundData):

    def __init__(self):
        self.input_data = pd.DataFrame()
        self.result_data = pd.DataFrame()
        self.errors = []

    def feed_data(self, surround_data):
        self.input_data = surround_data


class WranglingData(Stage):

    def __init__(self):
        self.processed_data = pd.DataFrame()

    # This function cleans the row containing empty field.
    def clean_empty_data(self):
        self.processed_data.dropna(inplace=True)

    # This function assigns the rank of each team.
    # One-hot encoding is another option for changing categorical to metric form in our example.
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
        self.predicted_output = pd.DataFrame()

    def combine_result(self, x_test, y_test, y_predicted):
        print("this is the x test data {}".format(type(x_test)))
        print("this is the y result data {}".format(type(y_test)))
        print("this is the predicted data {}".format(type(y_predicted)))

        # Concatenating x_test Dataframe and y_test panda series to a dataframe.
        self.predicted_output = pd.concat([x_test, y_test], axis=1)

        # pd.options.mode.chained_assignment = None #If copy slice warning occur due to chained assignments.
        # Adding the predicted Full Time Result in the test data.
        self.predicted_output['Predicted_FTR'] = y_predicted

        print(self.predicted_output)

    # Function to create the training and test data
    def train_test_data(self):
        feature_columns = ['HomeTeam', 'AwayTeam', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HR', 'AR']

        x_data = self.processed_data[feature_columns]
        y_data = self.processed_data['FTR']
        # print(x_data)
        # print(y_data)

        # This function splits data into 70% of training data and 30% of test data.
        # And returns the 2 sets of panda dataframe as train and test data features
        # and 2 sets of panda series as train and test data class.
        x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3, random_state=55)

        # This is the Logistic Regression model.
        # instantiate the model (using the default parameters)
        log_reg = LogisticRegression()
        # fit the model with data
        log_reg.fit(x_train, y_train)
        # This is the predicted data.
        y_predicted = log_reg.predict(x_test)

        # # This is the model created by Dbhatta.
        # dbhatta = DbhattaAlgorithm()
        # dbhatta.fit(x_train, y_train)
        # y_predicted = dbhatta.predict(x_test)

        print("This is the predicted data {0}".format(y_predicted))
        # Combining all the test data to get the final result.
        self.combine_result(x_test, y_test, y_predicted)

    def operate(self, surround_data, config):
        self.processed_data = surround_data.input_data
        self.train_test_data()
        surround_data.result_data = self.predicted_output
        print(surround_data.result_data)


class DisplayOutput(Stage):

    def display_histogram(self, histo_data, output_dir):
        # Display the histogram using matplotlib's pyplot.
        fig1, ax = plt.subplots(1, 2)
        histo_data.FTR.value_counts().plot("bar", ax=ax[0]).set_title("Real")
        histo_data.Predicted_FTR.value_counts().plot("bar", ax=ax[1]).set_title("Predicted")
        print("Please Check the displayed image and close it for proceeding further.")
        plt.show()

        # Saving plotted image to output folder
        fig1.savefig(output_dir + "/compare_result.png")
        plt.close()

    def prediction_report(self, real, prediction, output_dir):
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
        labels = ["H", "D", "A"]
        cnf_matrix = metrics.confusion_matrix(real, prediction, labels)
        print(cnf_matrix)
        print("The accuracy of the Logistic regression model is: {0}" .format(metrics.accuracy_score(real, prediction)))

        df_confusion = pd.DataFrame(cnf_matrix, index=["Home Win", "Draw", "Away Win"], columns=["Predicted Home Win", "Predicted Draw", "Predicted Away Win"])

        fig2 = plt.figure(2)
        sns.heatmap(df_confusion, annot=True, cbar=False)
        # Saving plotted image to output folder
        fig2.savefig(output_dir + "/confusion_matrix.png")
        plt.show()

    def operate(self, surround_data, config):
        # print(surround_data.result_data)
        # Save all the output of the test case in the "predicted output.csv" file in output folder.
        output_dir = config.get_path("surround.path_to_output")
        surround_data.result_data.to_csv(output_dir + "/test_output.csv")

        # Plot and save the histogram of actual Full Time Result and predicted in same plot.
        self.display_histogram(surround_data.result_data, output_dir)

        # Prediction statistics, especially confusion matrix plot and saving it to png file.
        self.prediction_report(surround_data.result_data.FTR, surround_data.result_data.Predicted_FTR, output_dir)
        print("Program is completed and for the output, check the output folder.")
