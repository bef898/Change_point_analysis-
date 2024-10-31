from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def initialize_arima_model(df, order=(1, 1, 1)):
    model = ARIMA(df['Price'], order=order)
    return model
def train_model(model):
    
    return model.fit()
def evaluate_model(df, predictions):
    """
    Evaluates the model using MAE and RMSE.
    Args:
        df (DataFrame): Original data with 'Price' column.
        predictions (Series): Predicted prices.
    Returns:
        dict: Evaluation metrics (MAE, RMSE).
    """
    mae = mean_absolute_error(df['Price'], predictions)
    rmse = np.sqrt(mean_squared_error(df['Price'], predictions))
    return {'MAE': mae, 'RMSE': rmse}
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
