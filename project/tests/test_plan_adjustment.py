import unittest
from project.agent.learning_agent import LearningAgent

class TestPlanAdjustment(unittest.TestCase):
    def setUp(self):
        self.agent = LearningAgent(user_id="test_adjustment")

    def test_low_progress_triggers_intensive_and_reduce(self):
        plan = self.agent.run("Learn Python", "python", 5, 1, 10)
        self.assertEqual(plan["reflection"]["adjustment"], "reduce_workload")
        self.assertLess(plan["reflection"]["actual"], 40)

    def test_high_progress_triggers_continue(self):
        plan = self.agent.run("Learn Python", "python", 5, 9, 10)
        self.assertEqual(plan["reflection"]["adjustment"], "continue")
        self.assertGreater(plan["reflection"]["actual"], 80)

    def test_reflection_records_expected_and_actual(self):
        plan = self.agent.run("Learn Python", "python", 5, 3, 10)
        self.assertIn("expected", plan["reflection"])
        self.assertIn("actual", plan["reflection"])
        self.assertIn("difference", plan["reflection"])

    def test_plan_has_multi_steps(self):
        plan = self.agent.run("Learn Python", "python", 5, 3, 10)
        self.assertIn("plan_steps", plan)
        self.assertGreater(len(plan["plan_steps"]), 1)

if __name__ == "__main__":
    unittest.main()