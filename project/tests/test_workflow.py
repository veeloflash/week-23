import unittest
from project.agent.learning_agent import LearningAgent
from project.agent.decision_engine import DecisionEngine

class TestWorkflow(unittest.TestCase):
    def setUp(self):
        self.agent = LearningAgent()
        self.decision = DecisionEngine()

    def test_decision_low_progress(self):
        self.assertEqual(self.decision.decide(20), "intensive")

    def test_decision_normal_progress(self):
        self.assertEqual(self.decision.decide(60), "normal")

    def test_decision_high_progress(self):
        self.assertEqual(self.decision.decide(90), "advance")

if __name__ == "__main__":
    unittest.main()
