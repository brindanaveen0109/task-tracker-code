import sys
from task_cli.task_manager import TaskManager

def main():
    task_manager = TaskManager()
    
    if len(sys.argv) < 2:
        print("Usage: task_tracker <action> [arguments...]")
        print("Actions:")
        print("  add <task_title>        - Add a new task")
        print("  update <id> <status>    - Update task status ('not-done', 'in-progress', 'done')")
        print("  delete <id>             - Delete a task")
        print("  list                    - List all tasks")
        print("  list-done               - List tasks marked as 'done'")
        print("  list-not-done           - List tasks marked as 'not-done'")
        print("  list-in-progress        - List tasks marked as 'in-progress'")
        return

    action = sys.argv[1]

    if action == "add":
        if len(sys.argv) < 3:
            print("Usage: task_tracker add <task_title>")
        else:
            print(task_manager.add_task(" ".join(sys.argv[2:])))
    
    elif action == "list":
        for i, task in enumerate(task_manager.list_tasks()):
            print(f"{i + 1}. {task['title']} - {task['status']}")
    
    elif action == "update":
        if len(sys.argv) < 4:
            print("Usage: task_tracker update <id> <status>")
        else:
            try:
                index = int(sys.argv[2])
                status = sys.argv[3]
                if status in ["not-done", "in-progress", "done"]:
                    print(task_manager.update_task(index, status))
                else:
                    print("Invalid status. Use 'not-done', 'in-progress', or 'done'.")
            except ValueError:
                print("ID must be a number.")
    
    elif action == "list-done":
        for i, task in enumerate(task_manager.list_tasks("done")):
            print(f"{i + 1}. {task['title']} - {task['status']}")
    
    elif action == "list-not-done":
        for i, task in enumerate(task_manager.list_tasks("not-done")):
            print(f"{i + 1}. {task['title']} - {task['status']}")
    
    elif action == "list-in-progress":
        for i, task in enumerate(task_manager.list_tasks("in-progress")):
            print(f"{i + 1}. {task['title']} - {task['status']}")
    
    elif action == "delete":
        if len(sys.argv) < 3:
            print("Usage: task_tracker delete <id>")
        else:
            try:
                index = int(sys.argv[2])
                print(task_manager.delete_task(index))
            except ValueError:
                print("ID must be a number.")
    
    else:
        print(f"Unknown action: {action}")

if __name__ == "__main__":
    main()
