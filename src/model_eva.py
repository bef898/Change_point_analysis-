from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt

def evaluate_arima_model(model, test_data, train_data):
    """
    Evaluate the ARIMA model on the test data.
    :param model: Trained ARIMA model.
    :param test_data: Testing portion of the time series data.
    :param train_data: Training portion of the time series data (for forecast range).
    :return: MSE and MAE scores
    """
    # Forecasting on test data length
    start = len(train_data)
    end = start + len(test_data) - 1
    forecast = model.predict(start=start, end=end)

    # Calculate error metrics
    mse = mean_squared_error(test_data, forecast)
    mae = mean_absolute_error(test_data, forecast)
    print(f"ARIMA Model Evaluation:\nMSE: {mse:.2f}, MAE: {mae:.2f}")
    
    # Plot forecast vs actual
    plt.figure(figsize=(10, 5))
    plt.plot(test_data.index, test_data, label="Actual Data")
    plt.plot(test_data.index, forecast, label="ARIMA Forecast", color="red")
    plt.title("ARIMA Model Forecast vs Actual Data")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.show()
    
    return mse, mae