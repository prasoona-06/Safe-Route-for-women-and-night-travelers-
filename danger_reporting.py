import json
import os
from datetime import datetime

# File where danger zone reports will be saved
DANGER_DATA_FILE = "danger_reports.json"

# Initialize the file if it doesn't exist
if not os.path.exists(DANGER_DATA_FILE):
    with open(DANGER_DATA_FILE, "w") as f:
        json.dump([], f)

def report_danger_zone(description, latitude, longitude, reporter_id="anonymous"):
    """
    Stores a danger zone report.
    Args:
        description (str): Description of the incident.
        latitude (float): Latitude of the danger location.
        longitude (float): Longitude of the danger location.
        reporter_id (str): Optional ID or name of the reporter.
    Returns:
        dict: The stored report.
    """
    report = {
        "description": description,
        "latitude": latitude,
        "longitude": longitude,
        "reporter_id": reporter_id,
        "timestamp": datetime.now().isoformat()
    }

    # Load existing reports
    with open(DANGER_DATA_FILE, "r") as f:
        reports = json.load(f)

    # Append the new report
    reports.append(report)

    # Save back to file
    with open(DANGER_DATA_FILE, "w") as f:
        json.dump(reports, f, indent=2)

    return report

def get_all_reports():
    """
    Returns all stored danger reports.
    """
    with open(DANGER_DATA_FILE, "r") as f:
        return json.load(f)
