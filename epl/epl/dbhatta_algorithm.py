# Developed by Dipesh Bhatta
# dbhatta@deakin.edu.au

import pandas as pd
from sklearn.preprocessing import normalize
from sklearn.cross_validation import train_test_split
from surround import Config


class DbhattaAlgorithm():
    def __init__(self):
        # home and away are the dataframes to store the weights of the features.
        # The num_features is the number of features in csv data. The balance is the number for balancing weight.
        self.home_weight = pd.DataFrame()
        self.away_weight = pd.DataFrame()
        self.total_home_weight = pd.DataFrame()
        self.total_away_weight = pd.DataFrame()
        self.num_features = 0
        self.balance = 0.005
        self.home_max = 1.0
        self.home_min = 0.025
        self.away_max = -0.025
        self.away_min = -1.0

    def set_initial_weight(self, wt):
        for i in range(0, int(self.num_features/2)):
            self.home_weight["'w_" + str(i) + "'"] = [wt]
            self.away_weight["'anti_w_" + str(i) + "'"] = [wt]

    # Function calculates the summation of feature inputs and its weight multiplication.
    # In row_data (2*i) gives the value of home index and (2*i+1) gives the index of its exact away feature index.
    def sum_feature_weight(self, row_data):
        sum_score = 0.0
        for i in range(0, int(self.num_features / 2)):
            sum_score += ((self.home_weight["'w_" + str(i) + "'"].values[0] * row_data[2 * i]) - (self.away_weight["'anti_w_" + str(i) + "'"]
                                                                                                  .values[0] * row_data[2*i+1]))
        return sum_score

    # def sum_predicted_weight(self, row_data):
    #     sum_score = 0.0
    #     for i in range(0, int(self.num_features / 2)):
    #         sum_score += ((self.total_home_weight["'w_" + str(i) + "'"].values[0] * row_data[2 * i]) - (self.total_away_weight["'anti_w_" + str(i) + "'"]
    #                                                                                               .values[0] * row_data[2*i+1]))
    #     return sum_score

    # Function return the min and max conditions required according to the row_result
    def check_weight_condition(self, row_result):
        if row_result == 'H':
            max_condition = self.home_max
            min_condition = self.home_min
        elif row_result == 'D':
            max_condition = self.home_min
            min_condition = self.away_max
        elif row_result == 'A':
            max_condition = self.away_max
            min_condition = self.away_min
        else:
            raise Exception('row_result should not be {0}'.format(row_result))
        return min_condition, max_condition

    def improve_weight(self, row_data, improve_weight_factor):
        # randomly choose a feature to improve and improve it's exact opposite feature as well.
        # selected_index = random.randint(0, int(self.num_features/2) -1)
        home_row_data = row_data[0::2].tolist()
        away_row_data = row_data[1::2].tolist()
        max_Hindex = home_row_data.index(max(home_row_data))
        min_Hindex = home_row_data.index(min(home_row_data))
        max_Aindex = away_row_data.index(max(away_row_data))
        min_Aindex = away_row_data.index(min(away_row_data))
        print(self.home_weight["'w_" + str(max_Hindex) + "'"])

        self.home_weight["'w_" + str(max_Hindex) + "'"] += improve_weight_factor
        self.home_weight["'w_" + str(min_Hindex) + "'"] -= improve_weight_factor

        self.away_weight["'anti_w_" + str(max_Aindex) + "'"] -= improve_weight_factor
        self.away_weight["'anti_w_" + str(min_Aindex) + "'"] += improve_weight_factor

    def fit(self, x_train, y_train):
        print("This is the starting of algorithm.")
        # Set number to  num_features
        self.num_features = len(x_train.keys())
        print(self.num_features)

        # Initial weight is set equal to each of the features equivalent to initial_weight.
        initial_weight = 1/(self.num_features/2)
        self.set_initial_weight(initial_weight)

        self.total_home_weight = self.home_weight.copy()
        self.total_away_weight = self.away_weight.copy()

        # Iterated through each x_train dataframe
        for index, row_data in x_train.iterrows():
            row_result = y_train[index]
            min_condition, max_condition = self.check_weight_condition(row_result)

            # adjust_weight is the flag which determine whether weight adjusting is still required or not.
            adjust_weight = True

            while adjust_weight:
                sum_score = self.sum_feature_weight(row_data)

                # This condition will never have max_condition more than 1 and min condition less than -1.
                # The main idea is around this theory.
                if (sum_score > min_condition) & (sum_score < max_condition):
                    adjust_weight = False
                elif sum_score < min_condition:
                    improve_weight_factor = self.balance
                    self.improve_weight(row_data, improve_weight_factor)
                elif sum_score > max_condition:
                    improve_weight_factor = - self.balance
                    self.improve_weight(row_data, improve_weight_factor)

            self.total_home_weight = self.total_home_weight.add(self.home_weight, fill_value=0).apply(lambda x: x/2)
            self.total_away_weight = self.total_away_weight.add(self.away_weight, fill_value=0).apply(lambda x: x/2)
            self.home_weight = self.total_home_weight.copy()
            self.away_weight = self.total_away_weight.copy()

            # # Initial weight is set equal to each of the features equivalent to initial_weight.
            # initial_weight = 1 / (self.num_features / 2)
            # self.set_initial_weight(initial_weight)

            # # There is mean_maker value for the total_home_weight and total_away_weight.
            # mean_maker = index + 1

        # # print(self.total_home_weight)
        # # print(self.total_away_weight)
        # # print("This is the mean_make {0}" .format(mean_maker))
        # self.total_home_weight = self.total_home_weight.apply(lambda x: x/mean_maker)
        # self.total_away_weight = self.total_away_weight.apply(lambda x: x/mean_maker)
        # print(self.total_home_weight)
        # print(self.total_away_weight)

    def result_category(self, predicted_value):
        if (predicted_value > self.home_min) & (predicted_value < self.home_max):
            return 'H'
        elif (predicted_value > self.away_max) & (predicted_value < self.home_min):
            return 'D'
        elif (predicted_value > self.away_min) & (predicted_value < self.away_max):
            return 'A'

    def predict(self, x_test):
        y_predicted = []
        for index, test_row in x_test.iterrows():
            predicted_value = self.sum_feature_weight(test_row)
            print("this is predicted value: {0}" .format(predicted_value))
            predicted_row = self.result_category(predicted_value)
            y_predicted.append(predicted_row)
        return y_predicted


# def main():
#     print("This works")
#     dbhatta = DbhattaAlgorithm()
#
#     raw_data = pd.read_csv("../data/raw_data.csv")
#
#     print(raw_data)
#     columns_to_standardize = [['home_shoot', 'away_shoot', 'home_shot_on_target', 'away_shot_on_target', 'home_possession',
#                                'away_possession', 'home_freekick', 'away_freekick']]
#     features = ['home_shoot', 'away_shoot', 'home_shot_on_target', 'away_shot_on_target', 'home_possession',
#                                'away_possession', 'home_freekick', 'away_freekick']
#
#     for each_col in columns_to_standardize:
#         print(each_col)
#         raw_data[each_col] = normalize(raw_data[each_col])
#
#     x_data = raw_data[features]
#     y_data = raw_data['FTR']
#
#     print(raw_data)
#     x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3, random_state=55)
#
#     dbhatta.fit(x_train, y_train)
#     print("this is the improve value of weight.")
#     print(dbhatta.total_home_weight)
#     print(dbhatta.total_away_weight)
#
#     temp = dbhatta.predict(x_test)
#     print(y_test)
#     print(temp)
#
#
# if __name__ == "__main__":
#     main()