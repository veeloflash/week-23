class DecisionEngine:
    def decide(self, progress, goal="", memory=None):
        if progress < 40:
            return "intensive"
        elif progress < 80:
            return "normal"
        else:
            return "advance"

    def select_tools(self, goal, progress, memory=None):
        """Choose the next tools from the goal, progress, and prior memory."""
        memory = memory or {}
        normalized_goal = goal.lower()
        previous_plan = memory.get("previous_plan", [])
        weak_topics = memory.get("weak_topics", [])
        tools = ["progress"]

        needs_plan = not previous_plan or memory.get("goal") != goal
        needs_questions = (
            any(word in normalized_goal for word in ("question", "practice", "quiz", "exercise"))
            or progress < 40
            or bool(weak_topics)
        )
        if needs_plan:
            tools.append("study_plan")
        if needs_questions:
            tools.append("question")
        return tools
