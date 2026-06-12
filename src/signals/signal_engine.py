import pandas as pd


def add_signals(master_df):

    demand_threshold = master_df["ND"].quantile(0.95)

    renewable_threshold = master_df["RENEWABLE"].quantile(0.10)

    carbon_threshold = master_df["CARBON_INTENSITY"].quantile(0.90)

    forecast_error_threshold = (
        master_df["Absolute_Error"].quantile(0.95)
    )

    master_df["Demand_Spike"] = (
        master_df["ND"] > demand_threshold
    )

    master_df["Forecast_Failure"] = (
        master_df["Absolute_Error"]
        > forecast_error_threshold
    )

    master_df["Low_Renewable_Window"] = (
        master_df["RENEWABLE"]
        < renewable_threshold
    )

    master_df["High_Carbon_Period"] = (
        master_df["CARBON_INTENSITY"]
        > carbon_threshold
    )

    master_df["Supply_Stress"] = (
        master_df["ND"]
        >
        master_df["GENERATION"] * 0.95
    )

    master_df["Generation_Surplus"] = (
        master_df["GENERATION"]
        >
        master_df["ND"] * 1.20
    )

    renewable_surge_threshold = (
        master_df["RENEWABLE"].quantile(0.90)
    )

    master_df["Renewable_Surge"] = (
        master_df["RENEWABLE"]
        >
        renewable_surge_threshold
    )

    demand_drop_threshold = (
        master_df["ND"].quantile(0.10)
    )

    master_df["Demand_Drop"] = (
        master_df["ND"]
        <
        demand_drop_threshold
    )

    return master_df