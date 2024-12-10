import sys
from task_cli.task_manager import add_task, list_tasks, update_task, delete_task, list_tasks_by_status

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
            print(add_task(" ".join(sys.argv[2:])))
    
    elif action == "list":
        for i, task in enumerate(list_tasks()):
            print(f"{i}. {task['title']} - {task['status']}")
    
    elif action == "update":
        if len(sys.argv) < 4:
            print("Usage: task_tracker update <index> <status>")
        else:
            try:
                index = int(sys.argv[2])
                status = sys.argv[3]
                if status in ["not done", "in progress", "done"]:
                    print(update_task(index, status))
                else:
                    print("Invalid status. Use 'not done', 'in progress', or 'done'.")
            except ValueError:
                print("Index must be a number.")
    
    elif action == "list-done":
        for i, task in enumerate(list_tasks_by_status("done")):
            print(f"{i}. {task['title']} - {task['status']}")
    
    elif action == "list-not-done":
        for i, task in enumerate(list_tasks_by_status("not done")):
            print(f"{i}. {task['title']} - {task['status']}")
    
    elif action == "list-in-progress":
        for i, task in enumerate(list_tasks_by_status("in progress")):
            print(f"{i}. {task['title']} - {task['status']}")
    
    elif action == "delete":
        if len(sys.argv) < 3:
            print("Usage: task_tracker delete <index>")
        else:
            try:
                index = int(sys.argv[2])
                print(delete_task(index))
            except ValueError:
                print("Index must be a number.")
    
    else:
        print(f"Unknown action: {action}")

if __name__ == "__main__":
    main()