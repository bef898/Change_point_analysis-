import matplotlib.pyplot as plt
import pandas as pd

def perform_eda(df):
  
    print(df.describe())  # Summary statistics
    
    # Plotting price trends over time
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Price'], label='Brent Oil Price')
    plt.title('Brent Oil Price Over Time')
    plt.xlabel('Year')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.show()
def feature_engineering(df):
    """
    Adds engineered features to the data.
    Args:
        df (DataFrame): Input data.
    Returns:
        DataFrame: Data with additional features.
    """
    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    # Extract year, month, and quarter
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Quarter'] = df['Date'].dt.quarter
    
    return df
def plot_time_series(data):
    """
    Plot the time series to analyze trends, seasonality, and volatility.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data, label='Brent Oil Prices')
    plt.title("Brent Oil Prices Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.show()

def plot_rolling_statistics(data, window=30):
    """
    Plot rolling mean and standard deviation to observe volatility.
    """
    rolling_mean = data.rolling(window).mean()
    rolling_std = data.rolling(window).std()

    plt.figure(figsize=(12, 6))
    plt.plot(data, label='Original')
    plt.plot(rolling_mean, label=f'{window}-day Rolling Mean', color='red')
    plt.plot(rolling_std, label=f'{window}-day Rolling Std Dev', color='green')
    plt.legend()
    plt.title("Rolling Mean & Standard Deviation")
    plt.show()
