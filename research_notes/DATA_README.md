# DATA_README

## Dataset Inventory

This project uses three publicly available electricity system datasets.

### Dataset 1: National Demand Data

Purpose:
Provides national electricity demand measurements and embedded renewable generation metrics.

Rows:
17,520

Columns:
22

Date Range:
2025-01-01 to 2025-12-31

Key Fields:

* ND
* TSD
* ENGLAND_WALES_DEMAND
* EMBEDDED_WIND_GENERATION
* EMBEDDED_SOLAR_GENERATION

---

### Dataset 2: Generation Mix Data

Purpose:
Provides generation mix, renewable generation, fossil generation, and carbon intensity information.

Rows:
305,579 (original)

Rows Used:
17,520 (filtered to 2025)

Columns:
34

Date Range:
2009-01-01 to 2026-06-07

Key Fields:

* GENERATION
* RENEWABLE
* FOSSIL
* CARBON_INTENSITY

---

### Dataset 3: Forecast Performance Data

Purpose:
Provides forecasted demand and actual demand values for forecasting performance analysis.

Rows:
89,086 (original)

Rows Used:
17,520 (filtered to 2025)

Columns:
11

Date Range:
2021-04-01 to 2026-04-30

Key Fields:

* Demand_Forecast
* Demand_Outturn
* Absolute_Error
* APE

---

## Data Quality Summary

* Missing Values: 0
* Duplicate Rows: 0
* Invalid Dates: 0

---

## Master Dataset

Datasets were integrated using a common Datetime field.

Integration Method:
Inner Join

Final Dataset Shape:
17,520 rows × 14 columns

Purpose:
Creates a unified operational dataset combining demand, generation, renewable contribution, carbon intensity, and forecast performance metrics.
