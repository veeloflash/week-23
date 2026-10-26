import unittest
from project.agent.learning_agent import LearningAgent

class TestAgent(unittest.TestCase):
    def setUp(self):
        self.agent = LearningAgent(user_id="test_agent")

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

    def test_agent_decision_is_recorded(self):
        plan = self.agent.run("Learn Python", "python", 5, 1, 10)
        self.assertIn("reflection", plan)
        self.assertIn("adjustment", plan["reflection"])

    def test_agent_multi_step_plan(self):
        plan = self.agent.run("Learn Python", "python", 5, 3, 10)
        self.assertIn("plan_steps", plan)
        self.assertGreaterEqual(len(plan["plan_steps"]), 2)

if __name__ == "__main__":
    unittest.main()