# Classes and their methods of Example - 2


#### 1. class FeedData(Stage)

       from surround import SurroundData, Stage
       import numpy as np
       from sklearn.svm import SVR
       from sklearn.preprocessing import StandardScaler
       import matplotlib.pyplot as plt
       import pandas as pd
       import csv


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


              def get_data(self):
              self.dta = pd.read_csv('config.yaml')
              self.dates = []
              self.prices = []
              self.x = [self.prices]
           

In this example, the 3 kernels - Linear, Polynomial and RBF of Vector Regression model are used.

The class SVRData(SurroundData) [ SVR - Support Vector Regression] is explained below:

**Pandas** has been imported as `pd`. The library **pandas** stands for "Python Data Analysis Library". **DataFrame** is  two-dimensional labelled data structure with columns of potentially different types, like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used **pandas** object.

The method `get_data(self)` reads the data from input file `AAPL.csv` and stores it to the lists dates and prices. It uses the with as block to open the file and assigns it to `csvfile.csv`. `FileReader` allows us to iterate over every row in our csv file. Furthermore, `next(csvFileReader)` skips column names.

`dates.append(int(row[0].split('-')[0]))` gets day of the month which is at index zero since dates are in the format [date]-[month]-[year].

`prices.append(float(row[1])) row[1]` is converted to float for more precision.
