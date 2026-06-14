# DATA_README

## Dataset Inventory

This project uses three publicly available electricity system datasets.

## Dataset Sources

### National Demand Data

Source: National Energy System Operator (NESO) Open Data Portal.

### Historic Generation Mix Data

Source: National Energy System Operator (NESO) Open Data Portal.

### Day Ahead Half-Hourly Demand Forecast Performance Data

Source: National Energy System Operator (NESO) Open Data Portal.

---

## Collection Method

The datasets were manually downloaded as CSV files from the NESO Open Data Portal and stored in the `data/raw` directory.

The selected datasets provide complementary information on:

* Electricity demand
* Electricity generation mix
* Forecasting performance

These datasets were integrated to create a unified operational analytics environment.

---

## Dataset Limitations

* Analysis is limited to data available for the year 2025.
* Regional-level demand and generation information is not available.
* No outage or asset-level operational data was provided.
* Signal thresholds are based on deterministic statistical rules rather than official operational policies.
* Forecast performance analysis is limited to the metrics available in the source dataset.

---

## Cleaning Decisions

The following preparation and cleaning steps were performed:

* Converted all date fields to datetime format.
* Created a common Datetime field using Settlement Date and Settlement Period.
* Filtered Generation Mix data to 2025.
* Filtered Forecast Performance data to 2025.
* Removed timezone information from Forecast timestamps to ensure alignment.
* Validated that no missing values were present.
* Validated that no duplicate records were present.
* Integrated datasets using an inner join on the Datetime field.


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
