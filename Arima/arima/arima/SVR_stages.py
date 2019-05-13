from surround import SurroundData, Stage
import numpy as np
from sklearn.svm import SVR
from datetime import date
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
        self.dta = pd.read_csv('/Users/saikrishna/Documents/GitHub/Surround_AI_Suqad_2/Arima/arima/data/AAPL.csv')



class ComputeForecast(SurroundData, Stage):
    def __init__(self):
        self.something = []

    def somp(self):
        print("this is fine")

    def predict_price(self, dates, prices):

        dates = np.reshape(dates, (len(dates), 1))
        svr_lin = SVR(kernel='linear', C=1e3)
        svr_poly = SVR(kernel='poly', C=1e3, degree=2)
        svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
        svr_rbf.fit(dates, prices)
        svr_lin.fit(dates, prices)
        svr_poly.fit(dates, prices)
        print(svr_rbf.predict(dates))

    def operate(self, surround_data, config):
        dates = []
        prices = []
        s_data = surround_data.dta
        with open('/Users/saikrishna/Documents/GitHub/Surround_AI_Suqad_2/Arima/arima/data/AAPL.csv', 'r') as csvfile:
            # csvFileReader allows us to iterate over every row in our csv file
            csvFileReader = csv.reader(csvfile)
            next(csvFileReader)  # skipping column names
            for row in csvFileReader:
                dates.append(int(row[0].split('-')[0]))  # Only gets day of the month which is at index 0
                prices.append(float(row[1]))
                self.predict_price(dates, prices)
                return








