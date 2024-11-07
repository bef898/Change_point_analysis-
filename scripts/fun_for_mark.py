# Importing Libraries
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.api import VAR
from statsmodels.tsa.regime_switching.markov_switching import MarkovSwitching
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns

# Main Class for Brent Oil Price Analysis
class BrentOilPriceAnalysis:
    
    def __init__(self, oil_data, economic_data):
        # Initialization with oil and economic data
        self.oil_data = oil_data
        self.economic_data = economic_data
        self.model_results = {}
        
    ### A. Data Preprocessing Module ###
    def preprocess_data(self):
       # Handle missing values by replacing with the mean value
       # self.oil_data = self.oil_data.fillna(self.oil_data.mean())
        self.economic_data = self.economic_data.fillna(self.economic_data.mean())
    
    # Merge the data based on the 'year' column
        merged_data = pd.merge(self.oil_data, self.economic_data, on='Year')
    
    # Standardize economic data for consistency in modeling
    # scaler = StandardScaler()
    # merged_data.iloc[:, 1:] = scaler.fit_transform(merged_data.iloc[:, 1:])
    
        self.processed_data = merged_data
        return self.processed_data

    ### B. EDA Module ###
    def perform_eda(self):
        """
        Function to perform EDA on the preprocessed data.
        - Includes univariate, bivariate, and correlation analysis.
        """
        print("Data Overview:")
        print(self.processed_data.describe())
        
        # Univariate Analysis: Plot oil price trends
        plt.figure(figsize=(10, 6))
        plt.plot(self.processed_data['Price'], label='Brent Oil Price')
        plt.title("Brent Oil Price Over Time")
        plt.xlabel("Year")
        plt.ylabel("Price")
        plt.legend()
        plt.show()
        
        # Correlation Heatmap between oil price and economic indicators
        plt.figure(figsize=(8, 6))
        sns.heatmap(self.processed_data.corr(), annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.show()
    
    ### C. Model Building Module ###
    
    # 1. ARIMA Model
    def train_arima(self, order=(1, 1, 1)):
        """
        Function to train an ARIMA model on Brent oil prices.
        """
        model = ARIMA(self.processed_data['Price'], order=order)
        self.model_results['ARIMA'] = model.fit()
        print("ARIMA Model trained.")
        return self.model_results['ARIMA']
    
    # 2. VAR Model
    def train_var(self, lag_order=1):
        """
        Function to train a Vector Autoregression (VAR) model.
        """
        model = VAR(self.processed_data)
        var_model = model.fit(lag_order)
        self.model_results['VAR'] = var_model
        print("VAR Model trained.")
        return self.model_results['VAR']
    
    # 3. Markov-Switching AR Model
    def train_markov_switching(self, data, k_regimes=2):
        """
        Function to train a Markov-Switching Autoregressive model.
        """
        model = MarkovSwitching(data, k_regimes=2, order=0)
        ms_model = model.fit()
        self.model_results['MarkovSwitching'] = ms_model
        print("Markov-Switching Model trained.")
        return self.model_results['MarkovSwitching']
    
    ### D. Evaluation Module ###
    def evaluate_model(self, model_name='ARIMA'):
        """
        Function to evaluate a model based on common time series metrics.
        """
        if model_name not in self.model_results:
            print(f"Model {model_name} is not trained.")
            return
        
        model = self.model_results[model_name]
        
        # Generate predictions
        predictions = model.predict(start=0, end=len(self.processed_data)-1)
        true_values = self.processed_data['Price']
        
        # Calculate metrics
        rmse = mean_squared_error(true_values, predictions, squared=False)
        mae = mean_absolute_error(true_values, predictions)
        
        print(f"{model_name} Model Evaluation:")
        print(f"RMSE: {rmse}")
        print(f"MAE: {mae}")
        return rmse, mae
    
    ### E. Insights Generation Module ###
    def generate_insights(self):
        """
        Function to analyze the relationship between oil prices and economic indicators.
        """
        # Print regression or model coefficients if available
        if 'VAR' in self.model_results:
            var_model = self.model_results['VAR']
            print("VAR Model Coefficients:")
            print(var_model.params)
        
        # Additional insights from correlation analysis
        correlation = self.processed_data.corr()
        print("Correlation between Brent Price and other factors:")
        print(correlation['Price'])
        
        # Recommendations could follow based on insights derived here


