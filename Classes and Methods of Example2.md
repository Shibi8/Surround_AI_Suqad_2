# Classes and Methods of Example - 2

1. class FeedData(Stage)

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


2. classs SVRData(SurroundData)

       class SVRData(SurroundData):
   
          def __init__(self):
           self.dta = pd.DataFrame()

          def getfunc(self):
     
             sth = 25
             return sth

         def get_data(self):
           
           self.dta = pd.read_csv('/Users/saikrishna/Documents/GitHub/Surround_AI_Suqad_2/Arima/arima/data/Apple_Data_300.csv')

