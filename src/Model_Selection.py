from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from arch import arch_model

def train_arima(train_data, order):
    """
    Train an ARIMA model using the training data.
    :param train_data: Training portion of the time series data.
    :param order: The (p, d, q) order parameters for ARIMA.
    :return: Fitted ARIMA model
    """
    model = ARIMA(train_data, order=order)
    arima_fit = model.fit()
    print(f"ARIMA model trained with order {order}")
    return arima_fit

def train_garch(train_data, order):
    """
    Train a GARCH model on the training data.
    :param train_data: Training portion of the time series data.
    :param order: The (p, q) order parameters for GARCH.
    :return: Fitted GARCH model
    """
    model = arch_model(train_data, vol='Garch', p=order[0], q=order[1])
    garch_fit = model.fit(disp="off")
    print(f"GARCH model trained with order {order}")
    return garch_fit
def generate_report(metrics, file_path='report.txt'):
    """
    Generates a report with model performance metrics.
    Args:
        metrics (dict): Dictionary containing evaluation metrics.
        file_path (str): Path to save the report.
    """
    with open(file_path, 'w') as file:
        for key, value in metrics.items():
            file.write(f"{key}: {value}\n")
    print(f"Report saved to {file_path}")
def communicate_results(df, metrics):
    """
    Displays results and saves plots as needed for stakeholder communication.
    Args:
        df (DataFrame): Data with predictions.
        metrics (dict): Performance metrics.
    """
    print("Model Performance Metrics:")
    for metric, value in metrics.items():
        print(f"{metric}: {value}")
    
    # Visualize predictions versus actual prices
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Price'], label='Actual Price')
    plt.plot(df['Date'], df['Predictions'], label='Predicted Price', linestyle='--')
    plt.title('Brent Oil Price Predictions vs. Actual Prices')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.show()
