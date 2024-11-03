import pandas as pd
from src.Model_Selection import train_arima, train_garch

def test_arima_training():
    data = pd.Series([100 + i for i in range(50)])
    model = train_arima(data,(1,1,1))
    assert model is not None

def test_garch_training():
    data = pd.Series([100 + (i % 10) for i in range(50)])
    model = train_garch(data,(1,1))
    assert model is not None
