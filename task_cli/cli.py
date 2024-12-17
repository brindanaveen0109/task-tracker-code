import argparse
from task_cli.task_manager import TaskManager

def main():
    task_manager = TaskManager()
    
    parser = argparse.ArgumentParser(
        prog="task_tracker", 
        description = "A CLI tool to manage the tasks."
    )

    subparsers = parser.add_subparsers(dest="command", help="Commands that you an use")
    
    add_parser = subparsers.add_parser("add", help="Add a new task to your list by passing arguments in the cli : add <task_title>")
    add_parser.add_argument("--description", "-d", required=True, help="Description of the task")
    
    list_parser = subparsers.add_parser("list", help="list all tasks or list tasks according to the status by passing arguments in the cli : list | list-done | list-not-done | list-in-progress")
    list_parser.add_argument("--status", "-s", choices=["not-done", "done", "in-progress"], help="Filter task by status")

    update_parser = subparsers.add_parser("update", help="Update the status of a task by passing argument in the command line with options : update --id <task-id> --status <task-status>")
    update_parser.add_argument("--id", "-i", type=int, required=True, help="Update the status of a task by ID")
    update_parser.add_argument("--status", "-s", choices=["not-done", "done", "in-progress"], required=True, help="New status of the task")

    delete_parser = subparsers.add_parser("delete", help="Delete a task by passing arguments in the command line: delete --id <task-id>")
    delete_parser.add_argument("--id", "-i", type=int, required=True, help="Task ID to delete")

    args = parser.parse_args()

    if args.command == "add":
        result = task_manager.add_task(args.description)

    elif args.command == "list":
        tasks = task_manager.list_tasks(args.status)
        if tasks:
            for i , task in enumerate(tasks):
                print(f"{i + 1}. {task['title']} - {task['status']}")
        else:
            print("No tasks found.")

    elif args.command == "update":
        result = task_manager.update_task(args.id, args.status)
        print(result)

    elif args.command == "delete":
        result = task_manager.delete_task(args.id)
        print(result)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
