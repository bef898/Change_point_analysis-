# data_collection.py
def load_data(file_path):
    """
    Load Brent oil price data from a CSV file.
    """
    data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
    print(f"Data loaded with {len(data)} records.")
    return data

# Usage
data = load_data(config['data_path'])
