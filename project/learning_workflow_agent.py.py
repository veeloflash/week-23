import random

class LearningTool:
    """Simple tool that returns study resources."""
    def get_resources(self, subject):
        database = {
            "math": ["Khan Academy Algebra", "Geometry Practice Set", "Exam-style problems"],
            "physics": ["Newton Laws Tutorial", "Energy Problems", "Exam simulations"],
            "english": ["Grammar workbook", "Reading comprehension set", "Essay templates"]
        }
        return database.get(subject.lower(), ["General study tips", "Time management guide"])


class ProgressTool:
    """Tool that simulates progress checking."""
    def check_progress(self):
        return random.choice(["good", "medium", "bad"])

class LearningWorkflowAgent:
    def __init__(self):
        self.learning_tool = LearningTool()
        self.progress_tool = ProgressTool()

    def generate_plan(self, goal):
        subject = goal.lower()
        resources = self.learning_tool.get_resources(subject)

        plan = {
            "goal": goal,
            "steps": [
                f"Study basic concepts of {goal}",
                f"Complete resource: {resources[0]}",
                f"Practice using: {resources[1]}",
                f"Finish advanced tasks: {resources[2]}"
            ]
        }
        return plan

    def adjust_plan(self, plan):
        progress = self.progress_tool.check_progress()

        if progress == "good":
            plan["steps"].append("Move to next chapter")
        elif progress == "medium":
            plan["steps"].append("Repeat practice problems")
        else:
            plan["steps"].append("Review fundamentals again")

        plan["progress"] = progress
        return plan

    def run_workflow(self, goal):
        print("=== Learning Workflow Agent ===")
        print(f"Goal received: {goal}")

        # Step 1: Generate plan
        plan = self.generate_plan(goal)
        print("\nGenerated Plan:")
        for step in plan["steps"]:
            print(" -", step)

        # Step 2: Check progress
        print("\nChecking progress...")
        plan = self.adjust_plan(plan)

        # Step 3: Final plan
        print("\nAdjusted Plan (based on progress):")
        for step in plan["steps"]:
            print(" -", step)

        print(f"\nProgress status: {plan['progress']}")
        print("=== Workflow Complete ===")

        return plan

if __name__ == "__main__":
    agent = LearningWorkflowAgent()
    agent.run_workflow("math")
