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

        start = 0
        end = -10
        df = pd.read_csv('/Users/saikrishna/Documents/GitHub/Surround_AI_Suqad_2/Arima/arima/data/Apple_Data_300.csv')[start:end]
        df.head()

        def get_data(df):

            data = df.copy()
            data['date'] = data['date'].str.split('-').str[2]
            data['date'] = pd.to_numeric(data['date'])
            return [data['date'].tolist(), data['close'].tolist()]

        dates, prices = get_data(df)


class ComputeForecast(SurroundData, Stage):

    def predict_price(dates, prices, x):
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

        return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]






















