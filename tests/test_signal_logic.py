import pandas as pd

signals = pd.read_csv(
    "outputs/signal_summary.csv"
)

assert len(signals) >= 8

print("Signal Validation Passed")