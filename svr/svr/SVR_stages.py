# In this program, I attempt to build three different models that
# predict the prices of Apple Stock
# then plot them all on a graph to compare the results

# The steps would be:
# 1. Install Dependencies
# 2. Collect Dataset
# 3. Write Script
# 4. Analyze Graph

# Step 1: The four dependencies include:
# pip3 install csv - To read data from the stock prices
# pip3 install numpy - To perform calculations
# pip3 install scikit-learn - build a predictive model
# pip3 install matplotlib - plot datapoints on the model to analyze

# Step 2: Collecting dataset (Apple stocks from the past 30 days)
# Go to finance.google.com
# Look up AAPL
# Select "Historical prices"
# Select "Download to spreadsheet"

# Step 3: Write Script
from surround import SurroundData, Stage
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import pandas as pd
import csv


class FeedData(Stage):

    def __init__(self):
        print("I am happy")

    def operate(self, surround_data, config):
        print("this is working fine")


class SVRData(SurroundData):
    def __init__(self):
        self.dta = pd.DataFrame()

    def get_data(self):
        self.dta = pd.read_csv('/Users/saikrishna/Documents/GitHub/Surround_AI_Suqad_2/svr/svr/config.yaml')



class ComputeForecast(SurroundData, Stage):
    def __init__(self):
        self.something = []

    def somp(self):
        print("this is fine")

    def predict_price(self, dates, prices):

        '''
        	Builds predictive model and graphs it
        	This function creates 3 models, each of them will be a type of support vector machine.
        	A support vector machine is a linear seperator. It takes data that is already classified and tries
        	to predict a set of unclassified data.
        	So if we only had two data classes it would look like this
        	It will be such that the distances from the closest points in each of the two groups is farthest away.
        	When we add a new data point in our graph depending on which side of the line it is we could classify it
        	accordingly with the label. However, in this program we are not predicting a class label, so we don't
        	need to classify instead we are predicting the next value in a series which means we want to use regression.
        	SVM's can be used for regression as well. The support vector regression is a type of SVM that uses the space between
        	data points as a margin of error and predicts the most likely next point in a dataset.
        	The predict_prices returns predictions from each of our models

        	'''

        dates = np.reshape(dates, (len(dates), 1)) # converts to a matrix from a vector
        # Linear support vector regression model.
        # Takes in 3 parameters:
        # 	1. kernel: type of svm
        # 	2. C: penalty parameter of the error term
        # 	3. gamma: defines how far too far is.

        # Two things are required when using an SVR, a line with the largest minimum margin
        # and a line that correctly seperates as many instances as possible. Since we can't have both,
        # C determines how much we want the latter.

        # Next we make a polynomial SVR because in mathfolklore, the no free lunch theorum states that there are no guarantees for one optimization to work better
        # than the other. So we'll try both.

        # Finally, we create one more SVR using a radial basis function. RBF defines similarity to be the eucledian distance between two inputs
        # If both are right on top of each other, the max similarity is one, if too far it is a zero
        svr_lin = SVR(kernel='linear', C=1e3)
        svr_poly = SVR(kernel='poly', C=1e3, degree=2)
        svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
        svr_rbf.fit(dates, prices)
        svr_lin.fit(dates, prices)
        svr_poly.fit(dates, prices)
        print(svr_rbf.predict(dates))
        print(svr_lin.predict(dates))
        print(svr_poly.predict(dates))

    def operate(self, surround_data, config):
        dates = []
        prices = []
        s_data = surround_data.dta
        with open('/Users/saikrishna/Documents/GitHub/Surround_AI_Suqad_2/svr/data/AAPL.csv', 'r') as csvfile:
            # csvFileReader allows us to iterate over every row in our csv file
            csvFileReader = csv.reader(csvfile)
            next(csvFileReader)  # skipping column names
            for row in csvFileReader:
                dates.append(int(row[0].split('-')[0]))  # Only gets day of the month which is at index 0
                prices.append(float(row[1])) # Convert to float for more precision
                self.predict_price(dates, prices)


                return



class PlotResult(SurroundData, Stage):

    def __init__(self):
        self.surround_data = pd.DataFrame()

    def plot(self):
        plt.scatter(dates, prices, color='black', label='Data')  # plotting the initial datapoints
        # The graphs are plotted with the help of SVR object in scikit-learn using the dates matrix as our parameter.
        # Each will be a distinct color and and give them a distinct label.
        plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')  # plotting the line made by the RBF kernel
        plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear model')  # plotting the line made by linear kernel
        plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial model')  # plotting the line made by polynomial kernel
        plt.xlabel('Date')  # Setting the x-axis
        plt.ylabel('Price')  # Setting the y-axis
        plt.title('Support Vector Regression for Apple Stock')  # Setting title
        plt.legend()  # Add legend
        plt.show()  # To display result on screen

        return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]  # returns predictions from each of our models


    def operate(self, surround_data, config):

         self.plot()
         return







