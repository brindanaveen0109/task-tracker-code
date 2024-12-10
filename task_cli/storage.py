import json
import sys
from pathlib import Path

# Path to the JSON file
taskfile = Path("data/tasks.json")

# Ensure the JSON file exists
if not taskfile.exists():
    with open(taskfile, "w", encoding='utf-8') as file:
        json.dump([], file)

# Load tasks from JSON
def load_tasks():
    try:
        with open(taskfile, "r", encoding='utf-8') as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

# Save tasks to JSON
def save_tasks(tasks):
    with open(taskfile, "w", encoding='utf-8') as file:
        json.dump(tasks, file, indent=4)