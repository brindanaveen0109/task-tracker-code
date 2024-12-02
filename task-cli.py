import json
import sys
from pathlib import Path

#add path to the json file
task_file = Path("tasks.json")

#check if the file exists or not
if not task_file.exists():
    with open(task_file, "w", encoding='utf-8') as f:
        json.dump([], f)

#function to load the task from the json file
def load_tasks():
    try:
        with open(task_file, "r", encoding='utf-8') as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

# Save tasks to JSON
def save_tasks(tasks):
    with open(task_file, "w", encoding='utf-8') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "status": "not done"})
    save_tasks(tasks)
    print(f"Task '{title}' added.")


#main cli logic
def main():
    if len(sys.argv) < 2:
        print("Usage: task_tracker <action> [arguments...]")
        print("Actions:")
        print("  add <task_title>        - Add a new task")
        return

action = sys.argv[1]

if action == "add":
    if len(sys.argv) < 3:
        print("Usage: task_tracker add <task_title>")
    else:
        add_task(" ".join(sys.argv[2:]))

if __name__ == "__main__":
    main()
