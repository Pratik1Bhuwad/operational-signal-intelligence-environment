import pandas as pd

kpis = pd.read_csv("outputs/kpi_summary.csv")

assert len(kpis) >= 10

print("KPI Validation Passed")