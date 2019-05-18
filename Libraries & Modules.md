**LIBRARIES:**

1. **Surround:**

Surround is a lightweight framework for serving machine learning pipelines in Python.

1. It is intended to be adaptable and simple to utilize.
2. It helps Data scientist by let them concentrate on the current issue instead on the development of code.
3. It is still being under constant and continuous development and expansion.

Surround has a pythonic interface and allows the developer to utilize this framework just as any of the already existed modules. This makes it a powerful framework of data-exploration purposes.

1. **SkLearn:**

Scikit-learn provides a range of supervised and unsupervised learning algorithms via a consistent interface in Python.It is licensed under a permissive simplified BSD license and is distributed under many Linux distributions, encouraging academic and commercial use.The library is built upon the SciPy (Scientific Python) that must be installed before you can use scikit-learn. This stack that includes:

·  **NumPy** , **SciPy** , **Matplotlib** , **IPython** , **Sympy** , **Pandas**

Extensions or modules for SciPy care conventionally named [SciKits](http://scikits.appspot.com/scikits). As such, the module provides learning algorithms and is named scikit-learn.The vision for the library is a level of robustness and support required for use in production systems. This means a deep focus on concerns such as easy of use, code quality, collaboration, documentation and performance.

**FUNCTIONS:**

- **Stage** : A usage of information change. Here is the place Surround Data is altered to accomplish the outcome that you need. Each stage is just meant to execut out a lot of related actions. First stage can be where you get ready information to be prepared and last stage can be the place your populate information to be sent back to the client.
- **Surround Data:** A sharable item between stages that holds vital data for each stage. A phase will read some data from Surround Data, process it, at that point set back new data that will be utilized by different stage(s). When you broaden this class, you can include as many number of variables as you require to enable you to change input data into output data. In any case, there are 4 center factors that are being utilized.

1. **Stage\_metadata** is information that can be used to identify a stage.
2. **Execution\_time** is recorded time to complete a process.
3. **Errors** is information to identify failure of a stage.
4. **Warnings** is information when transformation is not 100% right.

- **Sklearn.Preprocessing:**

The sklearn.preprocessing package provides several common utility functions and transformer classes to change raw feature vectors into a representation that is more suitable for the downstream estimators. Pre-processing refers to the transformations applied to your data before feeding it to the algorithm. In python, scikit-learn library has a pre-built functionality under [sklearn.preprocessing](http://scikit-learn.org/stable/modules/preprocessing.html). There are many more options for pre-processing

In general, learning algorithms benefit from standardization of the data set. If some outliers are present in the set, robust scalers or transformers are more appropriate.

- **Normalize** :

**Normalization**  is the process of  **scaling individual samples to have unit norm**. This process can be useful if you plan to use a quadratic form such as the dot-product or any other kernel to quantify the similarity of any pair of samples.

This assumption is the base of the [Vector Space Model](https://en.wikipedia.org/wiki/Vector_Space_Model) often used in text classification and clustering contexts.

- **Pandas:**

Pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with structured (tabular, multidimensional, potentially heterogeneous) and time series data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python. Additionally, it has the broader goal of becoming the most powerful and flexible open source data analysis / manipulation tool available in any language. It is already well on its way toward this goal.

- **MatplotLib** :

Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts.  It supports a very wide variety of graphs and plots namely - histogram, bar charts, power spectra, error charts etc. It is used along with NumPy to provide an environment that is an effective open source alternative for MatLab.

- **Train\_Test\_Split:**

The data we use is usually split into training data and test data. The training set contains a known output and the model learns on this data in order to be generalized to other data later on. We have the test dataset (or subset) in order to test our model&#39;s prediction on this subset.

**Parameters:**

**Arrays:** sequence of arrays or scipy.sparse matrices with same shape[0]

**Test\_Size:** float, int, or None (default is None)

**Train\_Size:** float, int, or None (default is None)

**Random\_State:** Pseudo-random number generator state used for random sampling.

**Returns:**

**        Splitting:** List containing train-test split of input array.

- **Logistic Regression:**

Machine Learning classification algorithm that is used to predict the probability of a categorical dependent variable. In logistic regression, the dependent variable is a binary variable that contains data coded as 1 (yes, success, etc.) or 0 (no, failure, etc.). In other words, the logistic regression model predicts P(Y=1) as a function of X.

- **Metrics** :

Different performance metrics are used to evaluate different Machine Learning Algorithms. For example a classifier used to distinguish between images of different objects; we can use classification performance metrics such as, Log-Loss, Average Accuracy, AUC, etc. If the machine learning model is trying to predict a stock price, then RMSE (rot mean squared error) can be used to calculate the efficiency of the mode

- **Label Encoder:**

labelEncoder encode labels with a value between 0 and n\_classes-1 where n is the number of distinct labels. If a label repeats it assigns the same value to as assigned earlier.

- **Time:**

This module provides various time-related functions.

- **Logging:**

** ** It emphatically advocates for treating log events as an event stream, and for sending that event stream to standard output to be handled by the application environment.