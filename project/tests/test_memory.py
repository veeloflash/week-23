import unittest
from project.memory.memory_manager import MemoryManager

class TestMemory(unittest.TestCase):
    def setUp(self):
        self.mem = MemoryManager("project/memory/test_memory.json")

    def test_memory_save_and_load(self):
        data = {
            "goal": "Learn Python",
            "completed_tasks": 3,
            "total_tasks": 10,
            "progress": 30,
            "previous_plan": ["task1"],
            "weak_topics": []
        }
        self.mem.save(data)
        loaded = self.mem.load()
        self.assertEqual(loaded["goal"], "Learn Python")
        self.assertEqual(loaded["progress"], 30)

if __name__ == "__main__":
    unittest.main()
