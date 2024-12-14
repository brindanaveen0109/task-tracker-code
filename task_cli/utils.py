from task_cli.storage import load_tasks

def validate_task_id(task_id):
    tasks = load_tasks()
    if 0 < task_id <= len(tasks):
        return True
    else:
        return False