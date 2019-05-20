# Classes and their methods of Example - 2


#### 1. class FeedData(Stage)

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

Here, the class `FeedData(Stage)` is nothing but a test class to check whether the integration of Vector Regression model into the Surround Framework is working fine or not.


#### 2. classs SVRData(SurroundData)

       class SVRData(SurroundData):
   
          def __init__(self):
           self.dta = pd.DataFrame()

          def getfunc(self):
     
             sth = 25
             return sth

         def get_data(self):
           
           self.dta = pd.read_csv('/Users/saikrishna/Documents/GitHub/Surround_AI_Suqad_2/Arima/arima/data/Apple_Data_300.csv')
           

In this example, the 3 kernels - Linear, Polynomial and RBF of Vector Regression model is used.

The class SVRData() [ SVR - Support Vector Regression] is explained below:

**Pandas** has been imported as `pd`. The library **pandas** stands for "Python Data Analysis Library". **DataFrame** is  two-dimensional labelled data structure with columns of potentially different types, like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used **pandas** object.

The `get_data(self)` is reading `config.yaml` from the input file.

The library pd reads data from the input file Apple_Data_300.csv and stores it to the dataframe.
