import pandas as pd

df = pd.read_csv("data/processed/master_operational_dataset.csv")

print("Missing Values Check")

print(df.isnull().sum().sum())