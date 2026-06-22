import pandas as pd

# Load signal intelligence table

signals = pd.read_csv(
    "D:/operational-signal-intelligence-environment/outputs/signal_intelligence_table.csv"
)

# Operational metadata

signal_metadata = {

    "Demand Spike": {
        "impact_area": "Grid Demand",
        "owner": "Regional Controller",
        "resolution_target": "2 Hours",
        "operational_consequence":
        "Potential grid stress due to elevated demand"
    },

    "Forecast Failure": {
        "impact_area": "Forecasting",
        "owner": "Forecast Analyst",
        "resolution_target": "4 Hours",
        "operational_consequence":
        "Reduced forecasting reliability"
    },

    "Low Renewable Window": {
        "impact_area": "Sustainability",
        "owner": "Energy Operations Team",
        "resolution_target": "6 Hours",
        "operational_consequence":
        "Increased dependence on fossil generation"
    },

    "High Carbon Period": {
        "impact_area": "Carbon Management",
        "owner": "Sustainability Manager",
        "resolution_target": "4 Hours",
        "operational_consequence":
        "Elevated carbon emissions"
    },

    "Supply Stress": {
        "impact_area": "Grid Capacity",
        "owner": "Regional Controller",
        "resolution_target": "1 Hour",
        "operational_consequence":
        "Potential supply shortfall"
    },

    "Generation Surplus": {
        "impact_area": "Generation Management",
        "owner": "Operations Team",
        "resolution_target": "6 Hours",
        "operational_consequence":
        "Excess generation capacity available"
    },

    "Renewable Surge": {
        "impact_area": "Renewable Operations",
        "owner": "Renewable Operations Team",
        "resolution_target": "4 Hours",
        "operational_consequence":
        "Exceptional renewable contribution"
    },

    "Demand Drop": {
        "impact_area": "Demand Management",
        "owner": "Operations Team",
        "resolution_target": "4 Hours",
        "operational_consequence":
        "Demand significantly below expected levels"
    }

}

# Enrich operational signals

signals["impact_area"] = signals["signal_name"].apply(
    lambda x: signal_metadata[x]["impact_area"]
)

signals["owner"] = signals["signal_name"].apply(
    lambda x: signal_metadata[x]["owner"]
)

signals["resolution_target"] = signals["signal_name"].apply(
    lambda x: signal_metadata[x]["resolution_target"]
)

signals["operational_consequence"] = signals["signal_name"].apply(
    lambda x: signal_metadata[x]["operational_consequence"]
)

# Export prioritized signals

signals.to_csv(
    "D:/operational-signal-intelligence-environment/outputs/signal_priority_table.csv",
    index=False
)

print("Signal priority table generated successfully")