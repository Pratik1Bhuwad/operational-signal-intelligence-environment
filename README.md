# Operational Signal Intelligence Environment

## Project Overview

The Operational Signal Intelligence Environment is a deterministic operational analytics and decision intelligence system built for electricity grid operations.

The project transforms raw operational data into actionable intelligence through:

* KPI generation
* Signal detection
* Explainable analytics
* Incident generation
* Escalation management
* Timeline reconstruction
* Executive reporting
* Operational control room dashboards

The objective is to help stakeholders rapidly understand:

* What is happening
* Why it is happening
* Who is responsible
* What action should be taken
* How urgent the situation is

---

# Project Architecture

Data → KPIs → Signals → Incidents → Escalations → Timeline → Dashboards → Executive Briefing

---

# Phase 1 — KPI Engine

Implemented 11 operational KPIs:

1. Average National Demand
2. Peak National Demand
3. Average Total Generation
4. Renewable Generation Share
5. Fossil Generation Share
6. Average Carbon Intensity
7. Forecast Accuracy
8. Average Forecast Error
9. Peak Renewable Generation
10. Peak Carbon Intensity
11. Peak Forecast Error

Output:

* kpi_summary.csv

---

# Phase 2 — Signal Intelligence Engine

Implemented 8 deterministic operational signals:

1. Demand Spike
2. Forecast Failure
3. Low Renewable Window
4. High Carbon Period
5. Supply Stress
6. Generation Surplus
7. Renewable Surge
8. Demand Drop

Each signal contains:

* timestamp
* signal_name
* severity
* reason
* supporting_metric
* confidence

Output:

* signal_intelligence_table.csv

---

# Phase 3 — Signal Prioritization Engine

Operational context was added to every signal.

Additional attributes:

* impact_area
* owner
* resolution_target
* operational_consequence

Example:

Demand Spike

* Impact Area: Grid Demand
* Owner: Regional Controller
* Resolution Target: 2 Hours

Output:

* signal_priority_table.csv

Total Prioritized Signals:

20,909

---

# Phase 4 — Incident Correlation Engine

Operational incidents are generated through deterministic signal correlation rules.

Examples:

Demand Spike + Supply Stress

→ GRID_STRESS_INCIDENT

Forecast Failure + Demand Spike

→ FORECAST_RISK_INCIDENT

Low Renewable Window + High Carbon Period

→ SUSTAINABILITY_INCIDENT

Output:

* incident_table.csv

Total Incidents:

5,526

---

# Phase 5 — Escalation Engine

Incidents are assigned ownership using a hierarchical escalation model.

Escalation Levels:

Level 1 — Operator

Level 2 — Supervisor

Level 3 — Regional Controller

Level 4 — Executive

Output:

* escalation_queue.csv

Ownership Distribution:

* Operator
* Supervisor
* Regional Controller
* Executive

---

# Phase 6 — Operational Timeline Engine

Operational events are reconstructed into a timeline.

Each incident generates:

* Incident Created
* Escalated
* Resolved

Output:

* incident_timeline.csv

Total Timeline Events:

16,578

---

# Phase 7 — Executive Summary Engine

Automated executive briefings are generated from operational activity.

Summary Includes:

* Current Operational State
* Critical Risks
* Immediate Actions
* Watchlist

Output:

* daily_executive_brief.txt

---

# Control Room Dashboards

Power BI dashboards were developed for three operational roles.

## Operator Console

Displays:

* Active Incidents
* Critical Incidents
* High Severity Incidents
* Incident Queue
* Pending Actions
* Incident Ownership
* Incident Severity Distribution

## Regional Controller Console

Displays:

* Regional Incidents
* High Severity
* Critical Severity
* Severity Distribution
* Regional Escalation Queue
* Incident Type Distribution


## Executive Dashboard

Displays:

* Total Incidents
* Critical Incidents
* Sustainability Incidents
* Forecast Risk Incidents
* Signal Volume
* Executive Escalations
* Top Risks
* Escalation Ownership
* Incident Timeline

Dashboard File:

Operational_Control_Room_Intelligence.pbix

or 

Open Folder:

dashboard_design

Review:

* Operator Console
* Regional Controller Console
* Executive Dashboard

---

# Repository Structure

```text
operational-signal-intelligence-environment/

├── control_room/
├── dashboard_design/
├── dashboards/
│   ├── Operational_Signal_Intelligence.pbix
│   └── Operational_Control_Room_Intelligence.pbix
├── data/
│   ├── raw/
│   └── processed/
├── escalations/
├── incident_engine/
├── notebooks/
├── outputs/
├── research_notes/
├── src/
│   ├── explainability/
│   ├── ingestion/
│   ├── kpis/
│   ├── reporting/
│   └── signals/
├── tests/
├── README.md
├── REVIEW_PACKET.md
└── REVIEW_PACKET_T1.md
```
---

## Dashboard Files

### Task 1 Dashboard

Operational_Signal_Intelligence.pbix

Contains:

- KPI Monitoring
- Signal Intelligence
- Explainability Analytics
- Data Health Monitoring

### Task 2 Dashboard

Operational_Control_Room_Intelligence.pbix

Contains:

- Operator Console
- Regional Controller Console
- Executive Dashboard

---

# Dashboard Cognition Research

Research was conducted on:

* Bloomberg Terminal
* Grafana
* Datadog
* Security Operations Centers (SOC)
* Emergency Operations Centers (EOC)

Topics Covered:

* Visual hierarchy
* Alert placement
* Executive cognition
* Dashboard layout principles
* Operational decision support

Documentation:

* dashboard_research.md
* dashboard_rationale.md

---

# Testing

Implemented Validation Tests:

* Missing Data Validation
* Duplicate Data Validation
* KPI Validation
* Signal Validation
* Schema Validation

Location:

tests/

---

# Technologies Used

* Python
* Pandas
* Jupyter Notebook
* Power BI
* Markdown
* Git
* GitHub

---

# Outputs Generated

* kpi_summary.csv
* signal_summary.csv
* signal_intelligence_table.csv
* signal_priority_table.csv
* incident_table.csv
* escalation_queue.csv
* incident_timeline.csv
* explainability_summary.csv
* daily_operational_summary.txt
* daily_executive_brief.txt
* data_health_summary.csv

---

# Success Criteria

The system succeeds when a stakeholder can determine:

* What is happening
* Why it matters
* Who is accountable
* What action is required

within seconds of opening the control room.

---

# Author

Pratik Bhuwad
