import unittest
from project.agent.learning_agent import LearningAgent

class TestAgent(unittest.TestCase):
    def setUp(self):
        self.agent = LearningAgent()

    def test_agent_run_basic(self):
        plan = self.agent.run(
            goal="Learn Python",
            subject="python",
            hours=5,
            completed=2,
            total=10
        )
        self.assertIn("tasks", plan)
        self.assertGreater(len(plan["tasks"]), 0)

    def test_agent_progress_calculation(self):
        plan = self.agent.run("Learn Math", "math", 4, 5, 10)
        mem = self.agent.memory.load()
        self.assertEqual(mem["progress"], 50)

if __name__ == "__main__":
    unittest.main()
