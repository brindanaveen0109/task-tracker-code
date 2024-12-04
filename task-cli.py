import json
import sys
from pathlib import Path

# Path to the JSON file
taskfile = Path("tasks.json")

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

# Add a new task
def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "status": "not done"})
    save_tasks(tasks)
    print(f"Task '{title}' added.")


# List all tasks
def list_tasks():
    tasks = load_tasks()
    if tasks:
        for i, task in enumerate(tasks):
            print(f"{i}. {task['title']} - {task['status']}")
    else:
        print("No tasks found.")


# Main CLI logic
def main():
    if len(sys.argv) < 2:
        print("Usage: task_tracker <action> [arguments...]")
        print("Actions:")
        print("  add <task_title>        - Add a new task")
        print("  update <index> <status> - Update task status ('not done', 'in progress', 'done')")
        print("  delete <index>          - Delete a task")
        print("  list                    - List all tasks")
        print("  list-done               - List tasks marked as 'done'")
        print("  list-not-done           - List tasks marked as 'not done'")
        print("  list-in-progress        - List tasks marked as 'in progress'")
        return

    action = sys.argv[1]

    if action == "add":
        if len(sys.argv) < 3:
            print("Usage: task_tracker add <task_title>")
        else:
            add_task(" ".join(sys.argv[2:]))
    
    elif action == "list":
        list_tasks()
    else:
        print(f"Unknown action: {action}")

if __name__ == "__main__":
    main()
