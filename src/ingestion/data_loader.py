import pandas as pd

def load_demand_data(path):
    return pd.read_csv(path)

def load_generation_data(path):
    return pd.read_csv(path)

def load_forecast_data(path):
    return pd.read_csv(path)