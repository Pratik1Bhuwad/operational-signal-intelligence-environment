import pandas as pd

# Load incident and escalation data

incident_df = pd.read_csv(
    "D:/operational-signal-intelligence-environment/outputs/incident_table.csv"
)

escalation_df = pd.read_csv(
    "D:/operational-signal-intelligence-environment/outputs/escalation_queue.csv"
)

# Operational metrics

total_incidents = len(incident_df)

critical_incidents = len(
    incident_df[
        incident_df["severity"] == "Critical"
    ]
)

high_incidents = len(
    incident_df[
        incident_df["severity"] == "High"
    ]
)

executive_escalations = len(
    escalation_df[
        escalation_df["owner"] == "Executive"
    ]
)

# Top risks

top_risks = (
    incident_df["incident_type"]
    .value_counts()
    .head(5)
)

# Immediate actions

actions = [

    "Monitor critical incidents",

    "Review executive escalations",

    "Investigate sustainability incidents",

    "Monitor forecast risk incidents",

    "Review grid stress conditions"
]

# Watchlist

watchlist = (
    incident_df["incident_type"]
    .value_counts()
    .tail(5)
)

# Executive brief

summary = f"""
EXECUTIVE OPERATIONAL BRIEF

CURRENT OPERATIONAL STATE

Total Incidents: {total_incidents}

Critical Incidents: {critical_incidents}

High Severity Incidents: {high_incidents}

Executive Escalations: {executive_escalations}


TOP RISKS

{top_risks.to_string()}


IMMEDIATE ACTIONS

1. Monitor critical incidents
2. Review executive escalations
3. Investigate sustainability incidents
4. Monitor forecast risk incidents
5. Review grid stress conditions


WATCHLIST

{watchlist.to_string()}
"""

# Export brief

with open(
    "D:/operational-signal-intelligence-environment/outputs/daily_executive_brief.txt",
    "w"
) as f:

    f.write(summary)

print(
    "Executive summary generated successfully"
)