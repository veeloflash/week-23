import unittest
from project.agent.learning_agent import LearningAgent

class TestToolSelection(unittest.TestCase):
    def setUp(self):
        self.agent = LearningAgent()

    def test_study_plan_tool_used(self):
        plan = self.agent.run("Learn Python", "python", 5, 1, 10)
        self.assertIn("subject", plan)
        self.assertEqual(plan["subject"], "python")

    def test_progress_tool_used(self):
        plan = self.agent.run("Learn Python", "python", 5, 3, 10)
        mem = self.agent.memory.load()
        self.assertEqual(mem["progress"], 30)

if __name__ == "__main__":
    unittest.main()
