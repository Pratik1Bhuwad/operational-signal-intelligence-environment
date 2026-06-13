# Operational Signal Intelligence Environment

## Project Overview

This project transforms raw electricity system data into actionable operational intelligence through KPI generation, signal detection, explainable analytics, automated reporting, and executive dashboarding.

The objective is to demonstrate how operational data can be converted into decision-support insights rather than simple visualizations.

---

## Project Structure

operational_signal_environment/

* data/
* notebooks/
* src/
* dashboard/
* outputs/
* research_notes/
* tests/

---

## Features

### KPI Engine

Implemented 11 operational KPIs:

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

### Signal Engine

Implemented 8 deterministic operational signals:

1. Demand Spike
2. Forecast Failure
3. Low Renewable Window
4. High Carbon Period
5. Supply Stress
6. Generation Surplus
7. Renewable Surge
8. Demand Drop

Each signal includes:

* timestamp
* signal_name
* severity
* reason
* supporting_metric
* confidence

### Explainability Layer

Each signal includes:

* What happened
* Why it occurred
* Operational concern
* Analyst investigation guidance

### Dashboard

Power BI dashboard includes:

* Executive Overview
* Signal Monitoring
* Explainability & Root Cause Analysis
* Data Health Monitoring

### Operational Summary Engine

Automated generation of daily operational summaries.

### Testing

Implemented:

* Missing Data Validation
* Duplicate Data Validation
* KPI Validation
* Signal Validation
* Schema Validation

---

## Technologies Used

* Python
* Pandas
* Jupyter Notebook
* Power BI
* Git
* GitHub

---

## Author

Pratik Bhuwad
