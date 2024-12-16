import json
from pathlib import Path

class Storage:
    """Handles loading and saving tasks to a JSON file."""
    def __init__(self, file_path="data/tasks.json"):
        self.file_path = Path(file_path)
        self.initialize_storage()

    def initialize_storage(self):
        """Ensure the JSON file exists and is initialized properly."""
        if not self.file_path.exists():
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump([], file)

    def load_tasks(self):
        """Load tasks from the JSON file."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_tasks(self, data):
        """Save tasks to the JSON file."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
