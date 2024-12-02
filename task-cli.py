import json
import sys
from pathlib import Path

#add path to the json file
task_file = Path("tasks.json")

#check if the file exists or not
if not task_file.exists():
    with open(task_file, "w", encoding='utf-8') as f:
        json.dump([], f)
    