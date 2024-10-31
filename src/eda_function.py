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
    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    # Extract year, month, and quarter
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    #df['week'] = df['Date'].dt.week
    df['day'] = df['Date'].dt.day
    
    return df



