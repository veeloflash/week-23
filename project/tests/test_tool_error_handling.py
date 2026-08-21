import unittest
from project.tools.progress_tool import ProgressTool

class TestToolErrorHandling(unittest.TestCase):
    def setUp(self):
        self.tool = ProgressTool()

    def test_zero_total_tasks(self):
        progress = self.tool.calculate(5, 0)
        self.assertEqual(progress, 0)

    def test_invalid_task_counts(self):
        with self.assertRaises(ValueError):
            self.tool.calculate(11, 10)
        with self.assertRaises(ValueError):
            self.tool.calculate(-1, 10)

if __name__ == "__main__":
    unittest.main()
