import pandas as pd

df = pd.read_csv(
    "data/processed/master_with_signals.csv"
)

required_columns = [

    "Datetime",
    "ND",
    "GENERATION",
    "RENEWABLE",
    "FOSSIL",
    "CARBON_INTENSITY"

]

for col in required_columns:

    assert col in df.columns

print("Schema Validation Passed")