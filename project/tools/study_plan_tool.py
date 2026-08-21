class StudyPlanTool:
    """Generate a structured study plan."""
    def generate(self, subject, goal, hours, progress=0, weak_topics=None, decision="normal"):
        if not isinstance(hours, (int, float)) or hours <= 0:
            raise ValueError("weekly hours must be greater than zero")

        weak_topics = weak_topics or []
        session_hours = round(hours / (3 if decision == "intensive" else 2), 1)
        tasks = [f"Study {subject} fundamentals for {session_hours} hours"]
        if weak_topics:
            tasks.append(f"Review weak topics: {', '.join(weak_topics)}")
        tasks.append(f"Practice {subject} exercises for {session_hours} hours")
        if progress >= 80:
            tasks.append(f"Apply {subject} knowledge to an advanced project")
        else:
            tasks.append(f"Review mistakes and retest {subject} concepts")
        tasks.append("Complete a weekly assessment")
        return {
            "subject": subject,
            "goal": goal,
            "weekly_hours": hours,
            "progress": progress,
            "decision": decision,
            "tasks": tasks
        }
