def train_test_split(data, test_size=0.2):
    """
    Split data into training and testing sets based on time series order.
    :param data: The cleaned time series data (should be univariate).
    :param test_size: Fraction of data to allocate to the test set (default is 20%).
    :return: train_data, test_data
    """
    # Select only the price column if needed
    price_data = data['Price'] if 'Price' in data.columns else data.squeeze()

    split_index = int(len(price_data) * (1 - test_size))
    train_data = price_data[:split_index]
    test_data = price_data[split_index:]
    
    print(f"Train-Test Split: {len(train_data)} training points, {len(test_data)} testing points.")
    return train_data, test_data

