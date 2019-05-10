from surround import SurroundData, Stage
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import pandas as pd


class FeedData(Stage):

    def __init__(self):
        print("I am happy")

    def operate(self, surround_data, config):
        print("this is working fine")


class SVRData(SurroundData, Stage):

    def get_data(self):
        dta = pd.read_csv('/Users/saikrishna/Documents/GitHub/Surround_AI_Suqad_2/Arima/arima/data/Apple_Data_300.csv')
        dta.Date = dta.Date.apply(pd.to_datetime)
        dates = np.array(dta.Date)
        prices = np.array(dta.Open)


class ComputeForecast(SurroundData, Stage):

    def predict_price(self, dates, prices, x, surround_data):

        dates = np.reshape(dates, (len(dates), 1))
        svr_lin = SVR(kernel='linear', C=1e3)
        svr_poly = SVR(kernel='poly', C=1e3, degree=2)
        svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
        svr_rbf.fit(dates, prices)
        svr_lin.fit(dates, prices)
        svr_poly.fit(dates, prices)
        plt.scatter(dates, prices, color='black', label='Data')
        plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
        plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear model')
        plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial model')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Support Vector Regression Apple Stock Model')
        plt.legend()
        plt.show()
        return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_rbf.predict(x)[0]
