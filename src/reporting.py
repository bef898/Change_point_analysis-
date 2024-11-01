import matplotlib.pyplot as plt
def plot_final_forecast(data, arima_forecast, garch_forecast=None):
    """
    Plot historical data along with ARIMA and GARCH forecasts.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data, label="Historical Data")
    plt.plot(arima_forecast, label="ARIMA Forecast", color="red")

    if garch_forecast is not None:
        plt.plot(garch_forecast, label="GARCH Volatility Forecast", color="green")

    plt.title("Brent Oil Price Forecast")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.show()


