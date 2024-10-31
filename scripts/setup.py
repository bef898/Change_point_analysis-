# setup.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from arch import arch_model

# Configuration settings (such as file paths, parameters)
config = {
    'data_path': r'C:\Users\befekadum\Documents\10x acadamy\week10\Change_point_analysis-\data\Copy of BrentOilPrices.csv',
    'forecast_horizon': 30,  # Number of days to forecast
    'arima_order': (1, 1, 1),
    'garch_order': (1, 1),
}
