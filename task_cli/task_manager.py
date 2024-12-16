from task_cli.storage import Storage
from task_cli.utils import validate_task_id

class TaskManager:
    """Manages tasks with add, update, delete, and list operations."""
    def __init__(self):
        self.storage = Storage()
    
    def add_task(self, title):
        """Add a new task."""
        tasks = self.storage.load_tasks()
        tasks.append({"title": title, "status": "not-done"})
        self.storage.save_tasks(tasks)
        return f"Task '{title}' added."

    def list_tasks(self, status=None):
        """List all tasks or filter by a specific status."""
        tasks = self.storage.load_tasks()
        if status:
            return [task for task in tasks if task["status"] == status]
        return tasks

    def update_task(self, index, status):
        """Update a task's status."""
        tasks = self.storage.load_tasks()
        index -= 1
        if validate_task_id(index + 1):
            tasks[index]["status"] = status
            self.storage.save_tasks(tasks)
            return f"Task '{tasks[index]['title']}' updated to '{status}'."
        else:
            return "Invalid task ID."

    def delete_task(self, index):
        """Delete a task."""
        index -= 1
        tasks = self.storage.load_tasks()
        if validate_task_id(index + 1):
            task = tasks.pop(index)
            self.storage.save_tasks(tasks)
            return f"Task '{task['title']}' deleted."
        else:
            return "Invalid task ID."
