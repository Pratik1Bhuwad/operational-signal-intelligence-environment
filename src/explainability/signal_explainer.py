import pandas as pd


def explain_signal(signal_name):

    explanations = {

        "Demand Spike": {
            "what_happened":
            "Electricity demand exceeded the defined spike threshold.",

            "why_triggered":
            "National demand was significantly higher than normal levels.",

            "operational_concern":
            "Potential grid stress and increased generation requirements.",

            "analyst_action":
            "Investigate demand drivers and capacity adequacy."
        },

        "Forecast Failure": {
            "what_happened":
            "Forecast error exceeded acceptable limits.",

            "why_triggered":
            "Actual demand deviated significantly from forecasted demand.",

            "operational_concern":
            "Reduced forecasting reliability.",

            "analyst_action":
            "Review forecasting assumptions and model inputs."
        },

        "Low Renewable Window": {
            "what_happened":
            "Renewable generation fell below threshold.",

            "why_triggered":
            "Wind and solar output were unusually low.",

            "operational_concern":
            "Greater dependence on fossil generation.",

            "analyst_action":
            "Monitor renewable availability and backup generation."
        },

        "High Carbon Period": {
            "what_happened":
            "Carbon intensity exceeded threshold.",

            "why_triggered":
            "Fossil fuel generation increased significantly.",

            "operational_concern":
            "Higher emissions and reduced sustainability performance.",

            "analyst_action":
            "Review generation mix and renewable availability."
        },

        "Supply Stress": {
            "what_happened":
            "Electricity demand approached available generation capacity.",

            "why_triggered":
            "Demand levels were close to total generation output.",

            "operational_concern":
            "Reduced operational flexibility and increased grid risk.",

            "analyst_action":
            "Monitor reserve margins and available generation capacity."
        },

        "Generation Surplus": {
            "what_happened":
            "Generation significantly exceeded demand.",

            "why_triggered":
            "Available generation was much higher than system demand.",

            "operational_concern":
            "Potential inefficiencies and excess supply conditions.",

            "analyst_action":
            "Review generation scheduling and demand forecasts."
        },

        "Renewable Surge": {
            "what_happened":
            "Renewable generation reached exceptionally high levels.",

            "why_triggered":
            "Wind and/or solar output was among the highest observed values.",

            "operational_concern":
            "Potential reduction in fossil generation requirements.",

            "analyst_action":
            "Evaluate renewable utilization and system balancing needs."
        },

        "Demand Drop": {
            "what_happened":
            "Electricity demand fell significantly below normal levels.",

            "why_triggered":
            "Demand was within the lowest observed operating range.",

            "operational_concern":
            "Possible under-utilization of generation resources.",

            "analyst_action":
            "Investigate demand patterns and operational scheduling."
        }
    }

    return explanations.get(
        signal_name,
        "No explanation available."
    )