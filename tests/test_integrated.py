import unittest
from task_cli.task_manager import add_task, list_tasks, update_task, delete_task, list_tasks_by_status

class TestTaskManagerIntegration(unittest.TestCase):
    def setUp(self):
        self.tasks = []
        list_tasks() 

    def test_integrated_task_management(self):
        add_task("Test task")
        tasks = list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['title'], "Test task")
        self.assertEqual(tasks[0]['status'], "not-done")
        update_task(1, "done")
        tasks = list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['status'], "done")
        tasks_done = list_tasks_by_status("done")
        self.assertEqual(len(tasks_done), 1)
        self.assertEqual(tasks_done[0]['title'], "Test task")
        self.assertEqual(tasks_done[0]['status'], "done")
        add_task("Test task 2")
        tasks = list_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[1]['title'], "Test task 2")
        self.assertEqual(tasks[1]['status'], "not-done")
        delete_task(1)
        tasks_after_delete = list_tasks()
        self.assertEqual(len(tasks_after_delete), 1)
        self.assertEqual(tasks_after_delete[0]['title'], "Test task 2")
        tasks_done_after_delete = list_tasks_by_status("done")
        self.assertEqual(len(tasks_done_after_delete), 0)

if __name__ == '__main__':
    unittest.main()
