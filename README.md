# Change_point_analysis-
Task 1: Data Analysis Workflow and Model Understanding for Brent Oil Prices
Project Overview
This project aims to analyze the historical Brent oil prices, identifying factors that contribute to fluctuations in prices. By leveraging time series modeling and statistical analysis, the goal is to uncover insights that inform stakeholders about price patterns and potential impacts of geopolitical and economic events.

Objectives of Task 1
Define the Data Analysis Workflow:

Outline the steps for data preprocessing, exploratory data analysis (EDA), and model training.
Establish an understanding of the dataset structure and key processes for effective analysis.
Understand the Model and Data:

Explore time series models like ARIMA and GARCH, suitable for price fluctuation analysis.
Review assumptions, limitations, and the expected outcomes of these models.
Project Structure
plaintext
Copy code
├── data/                   # Folder for storing data files
│   ├── brent_oil_prices.csv # Historical Brent oil prices dataset
├── notebooks/              # Jupyter notebooks for data exploration and EDA
│   ├── eda.ipynb            # Notebook for Task 1 exploratory data analysis
│    ├── model.ipynb
│    ├── changetimeAnalysis.ipynb
│   ├── edata_proccess_and_cleaning.ipynb
├── src/                    # Source code for modular analysis
│   ├── data_preprocessing.py   # Data cleaning and preprocessing scripts
│   ├── exploratory_analysis.py # Functions for EDA and plotting
│   ├── model_training.py       # Functions for ARIMA and GARCH model training
│   ├── model_evaluation.py     # Scripts for model evaluation and metrics
│   ├── forecasting.py          # Forecasting functions for future predictions
├── README.md               # Overview of the project and instructions
└── requirements.txt        # List of dependencies
Workflow Summary
1. Data Collection and Preprocessing
Objective: Load and clean the historical Brent oil prices dataset.
Process: Remove any missing values, detect outliers, and ensure consistent date formatting.
File: src/data_preprocessing.py
2. Exploratory Data Analysis (EDA)
Objective: Understand the trends, seasonality, and volatility in oil prices.
Process: Generate time series plots, rolling statistics, and autocorrelation functions (ACF/PACF).
File: notebooks/Task1_EDA.ipynb
3. Model Training and Selection
Objective: Apply time series models (ARIMA, GARCH) to capture price patterns.
Process: Use ARIMA for short-term forecasting and GARCH for volatility estimation.
File: src/model_training.py
4. Model Evaluation and Forecasting
Objective: Assess model accuracy and generate future price predictions.
Process: Evaluate model performance using MAE, MSE, and RMSE, and plot forecasts against actual data.
File: src/model_evaluation.py
5. Change Point Detection
Objective: Identify significant events or shifts in the oil price data.
Process: Use change-point detection to locate periods of drastic price changes, possibly due to economic or political events.
File: src/change_point_analysis.py
Key Models Used
ARIMA (Auto-Regressive Integrated Moving Average): Captures short-term trends and seasonality.
GARCH (Generalized Autoregressive Conditional Heteroskedasticity): Estimates price volatility, useful for assessing risk.
Change Point Analysis: Identifies time points where data properties shift significantly, which may indicate impactful external events.
Getting Started
Prerequisites
Ensure you have Python 3.8+ and install the required packages using:

bash
Copy code
pip install -r requirements.txt
Running the Analysis
Load and Preprocess Data: Run data_preprocessing.py to clean the dataset.
Conduct EDA: Explore the data by running Task1_EDA.ipynb.
Train and Evaluate Models: Use model_training.py and model_evaluation.py to apply and evaluate ARIMA and GARCH models.
Forecast and Detect Change Points: Use forecasting.py to make predictions and change_point_analysis.py for change-point detection.
Results and Insights
Exploratory Analysis: Identified initial trends and seasonality in oil prices.
Modeling Outcomes: ARIMA and GARCH models provide insights into price patterns and volatility.
Change Points: Significant dates were identified, correlating with key economic events.
Future Work
The next steps involve:

Expanding analysis with additional economic indicators.
Testing advanced models (e.g., VAR, LSTM) for complex pattern detection.
Applying the framework to other commodities.