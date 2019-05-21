**Class ModellingAndPrediction(Stage)**

**Introduction:**

The main purpose of this stage is to perform prediction task on the provided data frames. This stage consists of five different functions.

1. 1) **Initializing Function:**

![Init](https://raw.githubusercontent.com/Shibi8/Surround\_AI\_Suqad\_2/master/Images/init.png)

The  def \_\_init\_\_() function  initializes the two different variables for the data frames. One variable is for the processed data, which is in the streamline and the other is for the data frame on which the prediction function will be implemented.

1. 2) **Combining Results Function:**

![Combine](https://raw.githubusercontent.com/Shibi8/Surround\_AI\_Suqad\_2/master/Images/combine.png)

This function performs the task of combining multiple testing data subsets of the original dataset and then display the output as the predicted value.

1. 3) **Prediction Report Function:**

![PredictRepo](https://raw.githubusercontent.com/Shibi8/Surround\_AI\_Suqad\_2/master/Images/predict.png)

This function provides performance metrics and other metrics reports for the corresponding prediction models. This function predicts the total number of win for a particular team. It takes into account the total number of home and away wins to predict the result.

Furthermore, the function build a confusion matrix of home win, away wins &amp; draw matches and takes the mean of the home wins in real and predicted results.

1. 4) **Train Test Data Function:**

![TrainTest](https://raw.githubusercontent.com/Shibi8/Surround\_AI\_Suqad\_2/master/Images/TrainTest.png)

The main purpose of this function is to split the datasets into two categories i.e. training and testing datasets into defined ration for further processing. The datasets has been divided as 70% training and 30% testing data.  We have utilized logistic regression for our predictive analysis. Here, the test data set is utilized to test the model in consideration to examine its accuracy.

1. 5) **Operate Function:**

![Operate](https://raw.githubusercontent.com/Shibi8/Surround\_AI\_Suqad\_2/master/Images/operate.png)

This function is used to operate processed input data from a datasets onto a resulting output data matrix.