import matplotlib.pyplot as plt

def forecast_arima(model, steps):
    """
    Forecast future values using the ARIMA model.
    """
    forecast = model.forecast(steps=steps)
    plt.figure(figsize=(10, 5))
    plt.plot(forecast, label="ARIMA Forecast")
    plt.title("ARIMA Model Forecast")
    plt.legend()
    plt.show()
    return forecast

# forecasting.py
import matplotlib.pyplot as plt

def forecast_garch(model, steps):
    """
    Forecast volatility using the GARCH model and plot the forecasted volatility.
    :param model: Fitted GARCH model.
    :param steps: Number of future steps to forecast.
    :return: Forecasted volatility values.
    """
    forecast = model.forecast(horizon=steps)

    # Extract forecasted variance values for each time step in the horizon
    forecasted_volatility = forecast.variance.iloc[-1]  # Get the last row (latest forecast)

    # Plot the forecasted volatility
    plt.figure(figsize=(10, 5))
    plt.plot(forecasted_volatility, label="GARCH Forecasted Volatility")
    plt.title("GARCH Model Forecasted Volatility")
    plt.xlabel("Steps Ahead")
    plt.ylabel("Forecasted Variance")
    plt.legend()
    plt.show()
    
    return forecasted_volatility


