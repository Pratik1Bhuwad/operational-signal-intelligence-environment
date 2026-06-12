import pandas as pd


def generate_summary():

    signals = pd.read_csv(
        "outputs/signal_summary.csv"
    )

    kpis = pd.read_csv(
        "outputs/kpi_summary.csv"
    )

    summary = f"""
DAILY OPERATIONAL SUMMARY

Key Findings
------------
Average National Demand:
{kpis.loc[kpis['KPI']=='Average National Demand (MW)','Value'].values[0]:.2f} MW

Peak National Demand:
{kpis.loc[kpis['KPI']=='Peak National Demand (MW)','Value'].values[0]:.0f} MW

Emerging Risks
--------------
Demand Spike Events:
{signals.loc[signals['Signal']=='Demand Spike','Count'].values[0]}

Forecast Failure Events:
{signals.loc[signals['Signal']=='Forecast Failure','Count'].values[0]}

Operational Observations
------------------------
Low Renewable Windows:
{signals.loc[signals['Signal']=='Low Renewable Window','Count'].values[0]}

High Carbon Periods:
{signals.loc[signals['Signal']=='High Carbon Period','Count'].values[0]}

Priority Watch Areas
--------------------
Monitor demand spikes,
forecast failures,
renewable availability,
and carbon intensity trends.
"""

    with open(
        "outputs/daily_operational_summary.txt",
        "w"
    ) as file:

        file.write(summary)

    print(
        "Operational summary generated successfully."
    )


if __name__ == "__main__":

    generate_summary()