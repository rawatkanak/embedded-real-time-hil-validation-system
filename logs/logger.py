import json
import os

LOG_FILE = "logs/live_log.json"

def append_log(data):

    os.makedirs("logs", exist_ok=True)

    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)

    except:
        logs = []

    logs.append(data)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)