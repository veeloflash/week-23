import unittest
import os
from project.memory.memory_manager import MemoryManager

class TestMemory(unittest.TestCase):
    def setUp(self):
        self.mem = MemoryManager(user_id="test_user", base_path="project/memory")

    def tearDown(self):
        path = os.path.join("project/memory", "test_user.json")
        if os.path.exists(path):
            os.remove(path)

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

    def test_per_user_isolation(self):
        mem_a = MemoryManager(user_id="user_a", base_path="project/memory")
        mem_b = MemoryManager(user_id="user_b", base_path="project/memory")
        mem_a.save({"goal": "Learn Python", "progress": 50})
        mem_b.save({"goal": "Learn Math", "progress": 80})
        self.assertEqual(mem_a.load()["goal"], "Learn Python")
        self.assertEqual(mem_b.load()["goal"], "Learn Math")
        # Cleanup
        for uid in ("user_a", "user_b"):
            p = os.path.join("project/memory", f"{uid}.json")
            if os.path.exists(p):
                os.remove(p)

if __name__ == "__main__":
    unittest.main()
