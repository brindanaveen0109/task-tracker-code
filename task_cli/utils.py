from task_cli.storage import Storage

def validate_task_id(task_id):
    """Validate if a task ID is valid."""
    storage = Storage()
    tasks = storage.load_tasks()
    return 0 < task_id <= len(tasks)
