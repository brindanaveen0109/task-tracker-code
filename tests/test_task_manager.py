import unittest 
from task_cli.task_manager import add_task, list_tasks, update_task, delete_task, list_tasks_by_status

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tasks = []
    
    


    def test_add_task(self):
        add_task("Test task")
        self.tasks.append({'title':'Test task', 'status': 'not-done'})
        self.assertEqual(self.tasks[0]['title'], "Test task")

    def test_update_task(self):
        update_task(1, 'done')
        tasks = list_tasks()
        self.assertEqual(tasks[0]['status'], 'done')

    def test_list_task(self):
        tasks = list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['title'], "Test task")
        self.assertEqual(tasks[0]['status'], "not-done")
    
    def test_list_task_by_status(self):
        update_task(1, "done")
        tasks_done = list_tasks_by_status("done")
        self.assertEqual(len(tasks_done), 1)
        self.assertEqual(tasks_done[0]['title'], "Test task")

    def test_delete(self):
        add_task("Test task 1")
        delete_task(2)
        tasks = list_tasks()
        self.assertEqual(len(tasks), 1)


if __name__ == '__main__':
    unittest.main()