# Features Utilized of Surround:

### 1.	Modular Programming:

Division of a program/class into sub-classes and testing separately makes it easy to read, maintain and rely upon. When a modular system is created, several modules are built separately and more or less independently. The executable application will then be created by putting them together. In other words, Every file, which has the file extension .py and consists of proper Python code is a module. There is no special syntax required to make such a file a module. Usually, modules contain functions or classes, but there can be "plain" statements in them as well. These statements can be used to initialize the module. They are only executed when the module is imported. 


### 2.	Re-usability of code (Stages)

i. Same code can be used in other code to perform specific functionality as the code is divided into stages.

ii. Stage is an implementation of data transformation. Here is the place SurroundData is altered to accomplish the outcome that you need. Each stage is just meant to execute a set of related actions. First stage can be where you get ready information to be processed and last stage can be the place your populate information to be sent back to the client.


### 3.	Easier Access to Data (SurroundData)

i.	SurroundData is a sharable item between stages that holds vital data for each stage. A stage will read some data from SurroundData, process it, then at that point set back new data that will be utilized by different stage(s). When you expand this class, you can include as many number of variables as you require to enable you to change input data into output data. In any case, there are 4 center factors that are being utilized.
- stage_metadata is information that can be used to identify a stage.
- execution_time is recorded time to complete a process.
- errors is information to identify failure of a stage.
- warnings is information when transformation is not 100% right.

ii.	class SVRData(SurroundData):
    
    def __init__(self):
        self.dta = pd.DataFrame()

    def get_data(self):
        self.dta = pd.read_csv('/Users/saikrishna/Documents/GitHub/Surround_AI_Suqad_2/Arima/arima/data/AAPL (3).csv')


### 4.	Surround(): creates Pipeline

i.	It is a group of numerous stages or just an initial stage to change raw information into meaningful data. You can set the order of stages directly or by means of a config file. The config file enables you to characterize more than 1 pipeline execution and after that you can switch between them effectively.

ii.	Code snippets


### 5.	Config.yaml can be configured in the start for the whole project, Global variable, methods

i.	Path to data - 'Surround_AI_Suqad_2/svr/data/AAPL.csv'

ii.	An example from Apple Stock Price Predictions

    class SVRData(SurroundData):

    def __init__(self):
        self.dta = pd.DataFrame()


    def get_data(self):
        self.dta = pd.read_csv('config.yaml')
        self.dates = []
        self.prices = []
        self.x = [self.prices]


`config.yaml`

    output:
    text: Hello World

    image: svr
    company: yourcompany
    version: latest

    #Details of class inheriting from Wrapper
    wrapper-info: svr.wrapper.PipelineWrapper

    surround:
    path: '../data/AAPL.csv'

iii. Description

