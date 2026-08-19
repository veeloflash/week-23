class StudyPlanTool:
    """Generate a structured study plan."""
    def generate(self, subject, goal, hours):
        return {
            "subject": subject,
            "goal": goal,
            "weekly_hours": hours,
            "tasks": [
                f"Learn fundamentals of {subject}",
                f"Practice {subject} exercises",
                f"Review mistakes",
                f"Weekly assessment"
            ]
        }
