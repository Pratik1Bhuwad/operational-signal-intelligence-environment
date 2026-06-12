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
        }
    }

    return explanations.get(
        signal_name,
        "No explanation available."
    )