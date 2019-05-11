from surround import SurroundData, Stage
import numpy as np
from sklearn.svm import SVR
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd


class FeedData(Stage):

    def __init__(self):
        print("I am happy")

    def operate(self, surround_data, config):
        print("this is working fine")


class SVRData(SurroundData):
    def __init__(self):
        self.dta = pd.DataFrame()

    def getfunc(self):
        sth = 25
        return sth

    def get_data(self):
        self.dta = pd.read_csv('/Users/saikrishna/Documents/GitHub/Surround_AI_Suqad_2/Arima/arima/data/Apple_Data_300.csv')


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
        # print(svr)

    def operate(self, surround_data, config):
        s_data = surround_data.dta
        s_data.date = s_data.date.apply(pd.to_datetime)
        dates = np.array(s_data.date)
        prices = np.array(s_data.open)
        self.predict_price(dates, prices)

class PlotPredict(SurroundData, Stage)
    def __init__(self):
        self.dta = pd.DataFrame()

    def plot_it(self, x):
        plt.scatter(dates, prices, color='black', label='Data')  # plotting the initial datapoints
        plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')  # RBF kernel
        plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear model')  # linear kernel
        plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial model')  # polynomial kernel
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Support Vector Regression Apple Stock Model')
        plt.legend()
        plt.show()
        return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

    def operate(self, surround_data, config):

        self.plot_it()





