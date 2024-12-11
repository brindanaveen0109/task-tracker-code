from task_cli.storage import load_tasks, save_tasks

def add_task(title):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append({"title": title, "status": "not-done"})
    save_tasks(tasks)
    return f"Task '{title}' added."

def list_tasks_by_status(status):
    """List tasks filtered by a specific status."""
    tasks = load_tasks()
    return [task for task in tasks if task["status"] == status]

def list_tasks():
    """List all tasks."""
    return load_tasks()

def update_task(index, status):
    """Update a task's status."""
    tasks = load_tasks()
    index -= 1  
    if 0 <= index < len(tasks):
        tasks[index]["status"] = status
        save_tasks(tasks)
        return f"Task '{tasks[index]['title']}' updated to '{status}'."
    else:
        return "Invalid task index."

def delete_task(index):
    """Delete a task."""
    index = index - 1
    tasks = load_tasks()
    if 0 <= index < len(tasks) :
        task = tasks.pop(index)
        save_tasks(tasks)
        return f"Task '{task['title']}' deleted."
    else:
        print(index)
        return "Invalid task index."