import pandas as pd
from datetime import timedelta

# Load incident data

incident_df = pd.read_csv(
    "D:/operational-signal-intelligence-environment/outputs/incident_table.csv"
)

escalation_df = pd.read_csv(
    "D:/operational-signal-intelligence-environment/outputs/escalation_queue.csv"
)

# Timeline records

timeline_records = []

# Incident creation events

for _, row in incident_df.iterrows():

    timeline_records.append({

        "timestamp": row["timestamp"],

        "event_type":
            "Incident Created",

        "incident_id":
            row["incident_id"],

        "details":
            row["incident_type"]

    })

# Escalation events

for _, row in escalation_df.iterrows():

    timeline_records.append({

        "timestamp": row["timestamp"],

        "event_type":
            "Escalated",

        "incident_id":
            row["incident_id"],

        "details":
            row["owner"]

    })

# Resolution events

for _, row in escalation_df.iterrows():

    resolution_time = (
        pd.to_datetime(row["timestamp"])
        + timedelta(hours=2)
    )

    timeline_records.append({

        "timestamp":
            resolution_time,

        "event_type":
            "Resolved",

        "incident_id":
            row["incident_id"],

        "details":
            "Incident Closed"

    })

# Build timeline dataframe

timeline_df = pd.DataFrame(
    timeline_records
)

timeline_df["timestamp"] = pd.to_datetime(
    timeline_df["timestamp"]
)

timeline_df = timeline_df.sort_values(
    by="timestamp"
)

timeline_df = timeline_df.sort_values(
    by=["timestamp", "incident_id"]
).reset_index(drop=True)

# Export

timeline_df.to_csv(
    "D:/operational-signal-intelligence-environment/outputs/incident_timeline.csv",
    index=False
)

print(
    "Timeline generated successfully"
)