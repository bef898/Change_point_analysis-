import matplotlib.pyplot as plt
import pandas as pd

def perform_eda(df):
  
    print(df.describe())  # Summary statistics
    
    # Plotting price trends over time
    plt.figure(figsize=(12, 6))
    plt.plot(df['Year'], df['Price'], label='Brent Oil Price')
    plt.title('Brent Oil Price Over Time')
    plt.xlabel('Date')
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

