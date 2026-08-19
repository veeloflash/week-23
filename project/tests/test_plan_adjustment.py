import unittest
from project.agent.learning_agent import LearningAgent

class TestPlanAdjustment(unittest.TestCase):
    def setUp(self):
        self.agent = LearningAgent()

    def test_adjustment_low_progress(self):
        plan = self.agent.run("Learn Python", "python", 5, 1, 10)
        mem = self.agent.memory.load()
        self.assertLess(mem["progress"], 40)

    def test_adjustment_high_progress(self):
        plan = self.agent.run("Learn Python", "python", 5, 9, 10)
        mem = self.agent.memory.load()
        self.assertGreater(mem["progress"], 80)

if __name__ == "__main__":
    unittest.main()
