import pandas as pd

# Load prioritized signals

signals = pd.read_csv(
    "D:/operational-signal-intelligence-environment/outputs/signal_priority_table.csv"
)

signals["timestamp"] = pd.to_datetime(
    signals["timestamp"]
)

# Incident correlation rules

incident_rules = {

    ("Demand Spike", "Supply Stress"):
    "GRID_STRESS_INCIDENT",

    ("Forecast Failure", "Demand Spike"):
    "FORECAST_RISK_INCIDENT",

    ("Low Renewable Window", "High Carbon Period"):
    "SUSTAINABILITY_INCIDENT",

    ("Demand Spike", "High Carbon Period"):
    "PEAK_LOAD_EMISSIONS_INCIDENT",

    ("Supply Stress", "Forecast Failure"):
    "CAPACITY_PLANNING_INCIDENT",

    ("Demand Drop", "Generation Surplus"):
    "OVER_GENERATION_INCIDENT",

    ("Renewable Surge", "Generation Surplus"):
    "CURTAILMENT_RISK_INCIDENT",

    ("Demand Drop", "Low Renewable Window"):
    "DEMAND_ANOMALY_INCIDENT",

    ("Renewable Surge", "Demand Spike"):
    "RENEWABLE_SUPPORT_INCIDENT",

    ("Forecast Failure", "High Carbon Period"):
    "OPERATIONAL_RISK_INCIDENT"
}

# Group signals by timestamp

grouped = signals.groupby(
    "timestamp"
)["signal_name"].apply(list)

# Generate incidents

incidents = []

incident_counter = 1

for ts, signal_list in grouped.items():

    signal_set = set(signal_list)

    for rule_signals, incident_name in incident_rules.items():

        if set(rule_signals).issubset(signal_set):

            incidents.append({

                "incident_id":
                f"INC-{incident_counter:05d}",

                "timestamp":
                ts,

                "incident_type":
                incident_name,

                "contributing_signals":
                ", ".join(rule_signals)

            })

            incident_counter += 1

incident_df = pd.DataFrame(
    incidents
)

# Severity mapping

severity_map = {

    "GRID_STRESS_INCIDENT": "Critical",

    "FORECAST_RISK_INCIDENT": "High",

    "SUSTAINABILITY_INCIDENT": "Medium",

    "PEAK_LOAD_EMISSIONS_INCIDENT": "High",

    "CAPACITY_PLANNING_INCIDENT": "High",

    "OVER_GENERATION_INCIDENT": "Low",

    "CURTAILMENT_RISK_INCIDENT": "Medium",

    "DEMAND_ANOMALY_INCIDENT": "Medium",

    "RENEWABLE_SUPPORT_INCIDENT": "Low",

    "OPERATIONAL_RISK_INCIDENT": "High"
}

incident_df["severity"] = (
    incident_df["incident_type"]
    .map(severity_map)
)

# Business impact mapping

impact_map = {

    "GRID_STRESS_INCIDENT":
    "Risk of supply shortfall",

    "FORECAST_RISK_INCIDENT":
    "Reduced forecasting reliability",

    "SUSTAINABILITY_INCIDENT":
    "Elevated carbon emissions",

    "PEAK_LOAD_EMISSIONS_INCIDENT":
    "High demand with elevated emissions",

    "CAPACITY_PLANNING_INCIDENT":
    "Generation planning challenges",

    "OVER_GENERATION_INCIDENT":
    "Potential generation inefficiency",

    "CURTAILMENT_RISK_INCIDENT":
    "Potential renewable curtailment",

    "DEMAND_ANOMALY_INCIDENT":
    "Unexpected demand behavior",

    "RENEWABLE_SUPPORT_INCIDENT":
    "Renewables supporting demand",

    "OPERATIONAL_RISK_INCIDENT":
    "Multiple operational concerns"
}

incident_df["business_impact"] = (
    incident_df["incident_type"]
    .map(impact_map)
)

# Recommended response mapping

response_map = {

    "GRID_STRESS_INCIDENT":
    "Increase generation capacity and monitor demand",

    "FORECAST_RISK_INCIDENT":
    "Review forecasting models and assumptions",

    "SUSTAINABILITY_INCIDENT":
    "Investigate renewable availability",

    "PEAK_LOAD_EMISSIONS_INCIDENT":
    "Optimize generation mix",

    "CAPACITY_PLANNING_INCIDENT":
    "Review reserve capacity plans",

    "OVER_GENERATION_INCIDENT":
    "Reduce excess generation",

    "CURTAILMENT_RISK_INCIDENT":
    "Evaluate renewable curtailment actions",

    "DEMAND_ANOMALY_INCIDENT":
    "Investigate unusual demand behavior",

    "RENEWABLE_SUPPORT_INCIDENT":
    "Maintain renewable output",

    "OPERATIONAL_RISK_INCIDENT":
    "Perform operational risk assessment"
}

incident_df["recommended_response"] = (
    incident_df["incident_type"]
    .map(response_map)
)

# Escalation path mapping

path_map = {

    "Critical":
    "Operator → Supervisor → Regional Controller → Executive",

    "High":
    "Operator → Supervisor → Regional Controller",

    "Medium":
    "Operator → Supervisor",

    "Low":
    "Operator"
}

incident_df["escalation_path"] = (
    incident_df["severity"]
    .map(path_map)
)

# Export incidents

incident_df.to_csv(
    "D:/operational-signal-intelligence-environment/outputs/incident_table.csv",
    index=False
)

print(
    "Incident table generated successfully"
)