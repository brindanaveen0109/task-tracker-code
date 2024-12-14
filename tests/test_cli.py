import unittest
from pathlib import Path
from task_cli.storage import load_tasks, save_tasks

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.test_file = Path("data/tasks.json")
        
    def tearDown(self):
        if self.test_file.exists():
            self.test_file.unlink()
        
    def test_save_and_load_tasks(self):
        sample_task = {"title": "1", "status": "not-done"}
        save_tasks([sample_task])
        loaded_task = load_tasks()
        self.assertEqual([sample_task], loaded_task)

if __name__ == "__main__":
    unittest.main()