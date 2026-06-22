import pandas as pd

# Load incidents

incident_df = pd.read_csv(
    "D:/operational-signal-intelligence-environment/outputs/incident_table.csv"
)

# Assign escalation owner

def assign_escalation(severity):

    if severity == "Critical":
        return "Executive"

    elif severity == "High":
        return "Regional Controller"

    elif severity == "Medium":
        return "Supervisor"

    else:
        return "Operator"


incident_df["owner"] = (
    incident_df["severity"]
    .apply(assign_escalation)
)

# Notification groups

def notification_group(owner):

    mapping = {

        "Operator":
            "Operations Team",

        "Supervisor":
            "Operations Supervisor",

        "Regional Controller":
            "Regional Leadership",

        "Executive":
            "Executive Leadership"
    }

    return mapping[owner]


incident_df["notification_group"] = (
    incident_df["owner"]
    .apply(notification_group)
)

# Escalation paths

def escalation_path(owner):

    paths = {

        "Operator":
            "Operator",

        "Supervisor":
            "Operator → Supervisor",

        "Regional Controller":
            "Operator → Supervisor → Regional Controller",

        "Executive":
            "Operator → Supervisor → Regional Controller → Executive"
    }

    return paths[owner]


incident_df["escalation_path"] = (
    incident_df["owner"]
    .apply(escalation_path)
)

# Escalation queue output

escalation_queue = incident_df[
    [
        "incident_id",
        "timestamp",
        "incident_type",
        "severity",
        "owner",
        "notification_group",
        "escalation_path"
    ]
]

# Export

escalation_queue.to_csv(
    "D:/operational-signal-intelligence-environment/outputs/escalation_queue.csv",
    index=False
)

print("Escalation queue generated successfully")