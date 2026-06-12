import pandas as pd

df = pd.read_csv("data/processed/master_operational_dataset.csv")

print("Duplicate Records Check")

print(df.duplicated().sum())