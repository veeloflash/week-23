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

    def test_practice_goal_selects_questions(self):
        plan = self.agent.run("Practice Python questions", "python", 5, 8, 10)
        self.assertIn("question", plan["selected_tools"])
        self.assertIn("questions", plan)

    def test_advanced_progress_can_skip_new_plan(self):
        self.agent.run("Learn Python", "python", 5, 2, 10)
        plan = self.agent.run("Learn Python", "python", 5, 9, 10)
        self.assertNotIn("study_plan", plan["selected_tools"])

if __name__ == "__main__":
    unittest.main()
