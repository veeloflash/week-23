class Planner:
    """Decompose a learning goal into ordered subtasks (multi-step planning)."""

    def plan(self, goal, subject, hours, progress=0, weak_topics=None, decision="normal"):
        weak_topics = weak_topics or []
        steps = []
        step_num = 1

        # Step 1: Always start with review
        steps.append({
            "step": step_num,
            "action": "review",
            "description": f"Review {subject} fundamentals",
            "depends_on": None
        })
        step_num += 1

        # Step 2: Core practice based on decision
        if decision == "intensive":
            steps.append({
                "step": step_num,
                "action": "intensive_practice",
                "description": f"Intensive practice on {subject} basics ({hours}h)",
                "depends_on": "review"
            })
        elif decision == "normal":
            steps.append({
                "step": step_num,
                "action": "practice",
                "description": f"Practice {subject} exercises ({hours}h)",
                "depends_on": "review"
            })
        else:
            steps.append({
                "step": step_num,
                "action": "advanced_project",
                "description": f"Apply {subject} to an advanced project ({hours}h)",
                "depends_on": "review"
            })
        step_num += 1

        # Step 3: Targeted weak topics if any
        if weak_topics:
            steps.append({
                "step": step_num,
                "action": "targeted_review",
                "description": f"Focus on weak topics: {', '.join(weak_topics)}",
                "depends_on": steps[-1]["action"]
            })
            step_num += 1

        # Step 4: Assessment
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
