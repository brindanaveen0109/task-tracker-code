from task_cli.storage import load_tasks, save_tasks
from task_cli.utils import validate_task_id

class TaskManager:
    def add_task(self, title):
        """Add a new task."""
        tasks = load_tasks()
        tasks.append({"title": title, "status": "not-done"})
        save_tasks(tasks)
        return f"Task '{title}' added."

    def list_tasks_by_status(self, status):
        """List tasks filtered by a specific status."""
        tasks = load_tasks()
        return [task for task in tasks if task["status"] == status]

    def list_tasks(self):
        """List all tasks."""
        return load_tasks()

    def update_task(self, index, status):
        """Update a task's status."""
        tasks = load_tasks()
        index -= 1  
        if validate_task_id(index + 1):  
            tasks[index]["status"] = status
            save_tasks(tasks)
            return f"Task '{tasks[index]['title']}' updated to '{status}'."
        else:
            return "Invalid task ID."

    def delete_task(self, index):
        """Delete a task."""
        index = index - 1
        tasks = load_tasks()
        if validate_task_id(index + 1): 
            tasks = load_tasks()
            task = tasks.pop(index)
            save_tasks(tasks)
            return f"Task '{task['title']}' deleted."
        else:
            return "Invalid task ID."