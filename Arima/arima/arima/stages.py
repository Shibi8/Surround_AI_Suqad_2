from surround import Stage, SurroundData
import pandas as pd
import matplotlib.pyplot as plt
import numpy
import numpy as np
import pandas
import math
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from scipy.interpolate import spline
from sklearn.svm import SVR
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.arima_model import ARIMA
from scipy.stats import gaussian_kde
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose

class ArimaData(SurroundData):

    def __init__(self):
        self.input_data = pd.DataFrame()
        self.errors = []

    def feed_data(self, surround_data):
        self.input_data = surround_data


class DataInput(Stage):

    def __init__(self):
        self.input_data = pd.DataFrame()

    def init_stage(self, config):
        dir_path = config.get_path("surround.path_to_arima_data")
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

class DataRead(Stage):

#########Data Normalization
    def norm(x): return (x - np.min(x)) / (np.max(x) - np.min(x))

start = 0
end = -10
dataframe = pd.read_csv("/Users/saikrishna/Documents/GitHub/Surround_AI_Suqad_2/Arima/arima/arima/Data1/Data.csv")[start:end]
dataframe.head()
autocorrelation_plot(dataframe.ix[:, 4])

### ARIMA MODELLING and Dickey Fuller Test
model00 = ARIMA(np.array(dataframe.ix[:, 4]), dates=None, order=(2, 1, 0))
model11 = model00.fit(disp=1)
model11.summary()
model11.forecast()
resid9 = model11.resid
np.mean(abs(resid9)) / max(np.array(dataframe.ix[:, 4]))

x3 = resid9
x3 = x3[numpy.logical_not(numpy.isnan(x3))]
dftest13 = adfuller(x3, autolag='AIC')
dfoutput1 = pd.Series(dftest13[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
print('Dickey Fuller Test:\n', dfoutput1)

look_back = 200
start = 0
end = len(resid9)
lag = look_back
xx = np.array(resid9[start + lag:end])
yy = np.array(resid9[start:end - lag])
autocorrelation = np.corrcoef(xx, yy)
print('Autocorrelation of Residuals=', round(autocorrelation[0][1], 3))

plt.plot(resid9)
plt.title('Residuals arima')
plt.ylim(-50, 50)
plt.show()

print(pd.DataFrame(resid9).describe())

plt.hist(resid9)

density = gaussian_kde(resid9)
xs = np.linspace(-50, 50, len(resid9))
density.covariance_factor = lambda: .25
density._compute_covariance()

plt.plot(xs, density(xs))
plt.show()

### DELETING OUTLIERS ######
thre = 1.96
delete = np.where(resid9 < np.mean(resid9) - thre * np.std(resid9))[0]

train0 = np.delete(np.array(dataframe.ix[:, 4]), delete)
train = np.sqrt(train0)

plt.hist(train)

rollmean = pd.rolling_mean(train, window=20)
rollstd = pd.rolling_std(train, window=20)

ts_log0 = np.log(train)
ts_log = pd.DataFrame(ts_log0).dropna()
decomposition = seasonal_decompose(np.array(ts_log).reshape(len(ts_log), ), freq=100)

trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

z = np.where(seasonal == min(seasonal))[0]
period = z[2] - z[1]

look_back = period

plt.figure(figsize=(8, 8))
plt.subplot(411)
plt.plot(ts_log, label='Original')
plt.legend(loc='upper left')
plt.subplot(412)
plt.plot(trend, label='Trend', color='red')
plt.legend(loc='upper left')
plt.subplot(413)
plt.plot(seasonal, label='Seasonality', color='green')
plt.legend(loc='upper left')
plt.subplot(414)
plt.plot(residual, label='Residuals', color='black')
plt.legend(loc='upper left')
plt.tight_layout()

from statsmodels.tsa.stattools import adfuller

dftest = adfuller(train, autolag='AIC')
dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
dfoutput
'''Not Stationary'''

x = train0 * seasonal
x = x[numpy.logical_not(numpy.isnan(x))]
dftest1 = adfuller(x, autolag='AIC')
dfoutput1 = pd.Series(dftest1[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
print('Dickey Fuller Test:\n', dfoutput1)

train = train0 * seasonal
modelP2 = ARIMA(np.array(train)[-100:], order=(1, 1, 0))
model_fit2 = modelP2.fit(disp=-1, tol=1e-28, maxiter=100000)
pred71 = model_fit2.forecast()[0]
model_fit2.summary()

print('Precision=', float(pred71[-1] / (seasonal[-1] * train0[-1])))
print('Error=', 100 * (1 - float(pred71[-1] / (seasonal[-1] * train0[-1]))))
print('Real Stock Value', train[-1] / seasonal[-1])
print('Predicted Stock Value', pred71[-1] / seasonal[-1])

############## PLOTTING

train = train0 * seasonal

x = train0 * seasonal
x = x[numpy.logical_not(numpy.isnan(x))]
dftest1 = adfuller(x, autolag='AIC')
dfoutput1 = pd.Series(dftest1[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
print('Dickey Fuller Test:\n', dfoutput1)

for i in range(0, 10):
    if i < 2:
        modelP2 = ARIMA(np.array(train)[-100:], order=(1, 1, 0))
        model_fit2 = modelP2.fit(disp=-1, tol=1e-28, maxiter=100000)
        pred71 = model_fit2.forecast()[0]
        new = np.concatenate((train, pred71), axis=0)
        train = new
    else:
        modelP2 = ARIMA(np.array(train)[-100:], order=(1, 1, 0))
        model_fit2 = modelP2.fit(disp=-1, tol=1e-28, maxiter=100000)
        pred71 = model_fit2.forecast()[0]
        new = np.concatenate((train, pred71), axis=0)
        train = new

predicted = train / seasonal[-1]
predicted_ok = predicted[-11:]
dataframe3 = pd.read_csv('Apple_Data_Comparison.csv')
real_data = np.array(dataframe3.ix[end:end + 10, 4])

plt.figure(figsize=(8, 5))
line1, = plt.plot(predicted_ok, marker='o', linewidth=2, color='red', label='PREDICTION')
line2, = plt.plot(real_data, marker='o', linewidth=2, color='blue', label='REAL STOCK VALUE')
plt.annotate('TODAY', (0, 133))
for i in range(1, 10):
    plt.annotate('{0}%'.format(round(100 * (1 - (real_data / predicted_ok))[i], 2)), (i - .2, 133.5 + .3 * i))
plt.title('ARIMA TIME SERIES PREDICTION', fontsize=20)
plt.ylabel('Stock Value', fontsize=20)
plt.xlabel('Future Predictions (error)', fontsize=20)
plt.legend([line1, line2], loc='upper left')
plt.show()

print('Mean error:', 100 * np.mean(abs(real_data - predicted_ok)) / real_data[-1], 'percent')


