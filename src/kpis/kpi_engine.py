def calculate_kpis(master_df):

    kpis = {

        "Average National Demand (MW)":
            master_df["ND"].mean(),

        "Peak National Demand (MW)":
            master_df["ND"].max(),

        "Average Total Generation (MW)":
            master_df["GENERATION"].mean(),

        "Renewable Generation Share (%)":
            (
                master_df["RENEWABLE"].sum()
                /
                master_df["GENERATION"].sum()
            ) * 100,

        "Fossil Generation Share (%)":
            (
                master_df["FOSSIL"].sum()
                /
                master_df["GENERATION"].sum()
            ) * 100,

        "Average Carbon Intensity":
            master_df["CARBON_INTENSITY"].mean(),

        "Forecast Accuracy (%)":
            (
                1 -
                (
                    master_df["Absolute_Error"].mean()
                    /
                    master_df["Demand_Outturn"].mean()
                )
            ) * 100
    }

    return kpis