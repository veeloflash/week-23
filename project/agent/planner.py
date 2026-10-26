class Planner:
    """Decompose a learning goal into ordered subtasks (multi-step planning)."""

    def plan(self, goal, subject, hours, progress=0, weak_topics=None, decision="normal"):
        weak_topics = weak_topics or []
        steps = []
        step_num = 1

        steps.append({
            "step": step_num,
            "action": "review",
            "description": "Review " + subject + " fundamentals",
            "depends_on": None
        })
        step_num += 1

        if decision == "intensive":
            steps.append({
                "step": step_num,
                "action": "intensive_practice",
                "description": "Intensive practice on " + subject + " basics (" + str(hours) + "h)",
                "depends_on": "review"
            })
        elif decision == "normal":
            steps.append({
                "step": step_num,
                "action": "practice",
                "description": "Practice " + subject + " exercises (" + str(hours) + "h)",
                "depends_on": "review"
            })
        else:
            steps.append({
                "step": step_num,
                "action": "advanced_project",
                "description": "Apply " + subject + " to an advanced project (" + str(hours) + "h)",
                "depends_on": "review"
            })
        step_num += 1

        if weak_topics:
            steps.append({
                "step": step_num,
                "action": "targeted_review",
                "description": "Focus on weak topics: " + ", ".join(weak_topics),
                "depends_on": steps[-1]["action"]
            })
            step_num += 1

        steps.append({
            "step": step_num,
            "action": "assess",
            "description": "Complete weekly assessment",
            "depends_on": steps[-1]["action"]
        })

        return {
            "goal": goal,
            "subject": subject,
            "total_steps": len(steps),
            "steps": steps
        }