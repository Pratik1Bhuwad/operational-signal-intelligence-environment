# Data Profiling Report

## Dataset 1: National Demand Data

Rows: 17,520

Columns: 22

Date Range: 2025-01-01 to 2025-12-31

Missing Values: 0

Duplicate Rows: 0

Observations:

* Contains national demand metrics.
* Includes embedded wind and solar generation.
* Includes interconnector flow information.
* Suitable for demand analysis and operational signal generation.

---

## Dataset 2: Generation Mix Data

Rows: 305,579

Columns: 34

Date Range: 2009-01-01 to 2026-06-07

Missing Values: 0

Duplicate Rows: 0

Observations:

* Contains fuel mix information.
* Includes renewable and fossil generation.
* Includes carbon intensity metrics.
* Suitable for generation mix and sustainability KPIs.

---

## Dataset 3: Forecast Performance Data

Rows: 89,086

Columns: 11

Date Range: 2021-04-01 to 2026-04-30

Missing Values: 0

Duplicate Rows: 0

Observations:

* Contains forecast vs actual demand.
* Includes forecast error metrics.
* Suitable for operational forecasting signals.



## Data Preparation Summary

### Date Conversion

Converted date columns to datetime format:

- SETTLEMENT_DATE
- DATETIME
- Datetime

Reason:
To enable time-based analysis and dataset integration.

### Data Filtering

Generation Mix dataset filtered to 2025.

Forecast Performance dataset filtered to 2025.

Reason:
National Demand dataset contains only 2025 records. Filtering ensures consistent time coverage across all datasets.

### Timestamp Creation

Created a new Datetime column in the National Demand dataset using:

- SETTLEMENT_DATE
- SETTLEMENT_PERIOD

Reason:
Generation Mix and Forecast datasets already contained timestamps, while Demand data used settlement periods. Creating a common timestamp enables dataset integration.

### Data Quality Results

- Missing Values: 0
- Duplicate Rows: 0
- Invalid Dates: 0


### Timestamp Standardization

During data integration validation, the Forecast dataset used UTC timezone-aware timestamps (`datetime64[ns, UTC]`) while Demand and Generation datasets used timezone-naive timestamps (`datetime64[ns]`).

To ensure consistent joins and temporal alignment, timezone information was removed from the Forecast dataset before integration.

## Data Integration Summary

Three datasets were integrated using a common Datetime field.

Datasets:
- National Demand Data
- Generation Mix Data
- Forecast Performance Data

Integration Method:
- Inner Join on Datetime

Result:
- Master Operational Dataset

Rows:
17520

Purpose:
Provides a unified operational view combining demand, generation, renewable contribution, carbon intensity, and forecasting performance.


## KPI Engine Summary

The KPI Engine was developed using the Master Operational Dataset.

KPIs Implemented:

1. Average National Demand (MW)
2. Peak National Demand (MW)
3. Average Total Generation (MW)
4. Renewable Generation Share (%)
5. Fossil Generation Share (%)
6. Average Carbon Intensity (gCO₂/kWh)
7. Forecast Accuracy (%)
8. Average Forecast Error (MW)
9. Peak Renewable Generation (MW)
10. Peak Carbon Intensity (gCO₂/kWh)
11. Peak Forecast Error (MW)

Purpose:

The KPI Engine provides operational visibility into demand, generation mix, sustainability performance, and forecast quality.


## Signal Engine Summary

Operational signals were developed to identify important grid events and operational conditions.

Signals Implemented:

1. Demand Spike

   * Trigger: Demand exceeds 95th percentile.

2. Forecast Failure

   * Trigger: Absolute forecast error exceeds 2000 MW.

3. Low Renewable Window

   * Trigger: Renewable share falls below 20%.

4. High Carbon Period

   * Trigger: Carbon intensity exceeds 200 gCO₂/kWh.

Purpose:

The Signal Engine converts raw operational data into actionable alerts that can support operational monitoring and decision-making.


## Signal Engine Results

Signal Occurrences:

- Demand Spike: 876
- Forecast Failure: 718
- Low Renewable Window: 2759
- High Carbon Period: 2270

Output Files:

- signal_summary.csv
- master_with_signals.csv

Purpose:

The Signal Engine transformed operational measurements into actionable monitoring signals that can be used for alerting, dashboarding, and root-cause analysis.