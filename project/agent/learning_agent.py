from project.tools.progress_tool import ProgressTool
from project.tools.study_plan_tool import StudyPlanTool
from project.tools.question_tool import QuestionTool
from project.tools.registry import ToolRegistry
from project.agent.decision_engine import DecisionEngine
from project.agent.reflection import ReflectionEngine
from project.memory.memory_manager import MemoryManager

class LearningAgent:
    def __init__(self):
        self.progress_tool = ProgressTool()
        self.study_tool = StudyPlanTool()
        self.question_tool = QuestionTool()
        self.decision_engine = DecisionEngine()
        self.reflection_engine = ReflectionEngine()
        self.memory = MemoryManager()
        self.registry = ToolRegistry()
        self.registry.register("progress", self.progress_tool)
        self.registry.register("study_plan", self.study_tool)
        self.registry.register("question", self.question_tool)

    def run(self, goal, subject, hours, completed, total):
        print("=== Learning Workflow Agent ===")

        if not isinstance(goal, str) or not goal.strip():
            raise ValueError("goal must not be empty")
        if not isinstance(subject, str) or not subject.strip():
            raise ValueError("subject must not be empty")

        # Load memory
        mem = self.memory.load()

        progress = self.registry.execute("progress", "calculate", completed=completed, total=total)
        print(f"Progress: {progress}%")

        decision = self.decision_engine.decide(progress, goal, mem)
        print(f"Decision: {decision}")

        selected_tools = self.decision_engine.select_tools(goal, progress, mem)
        print(f"Selected tools: {', '.join(selected_tools)}")
        plan = {"subject": subject, "goal": goal, "weekly_hours": hours, "tasks": []}
        tool_errors = []
        if "study_plan" in selected_tools:
            try:
                plan = self.registry.execute(
                    "study_plan", "generate", subject=subject, goal=goal, hours=hours,
                    progress=progress, weak_topics=mem.get("weak_topics", []), decision=decision
                )
                print("Generated Plan:", plan)
            except (TypeError, ValueError, OSError) as error:
                tool_errors.append(f"study_plan: {error}")

        if "question" in selected_tools:
            try:
                level = "advanced" if decision == "advance" else "beginner"
                plan["questions"] = self.registry.execute(
                    "question", "get_questions", subject=subject, level=level,
                    weak_topics=mem.get("weak_topics", [])
                )
            except (TypeError, ValueError, OSError) as error:
                tool_errors.append(f"question: {error}")

        reflection = self.reflection_engine.reflect(
            progress, previous_progress=mem.get("progress"), weak_topics=mem.get("weak_topics", [])
        )
        plan["selected_tools"] = selected_tools
        plan["reflection"] = reflection
        plan["tool_errors"] = tool_errors
        print("Reflection:", reflection["message"])

        mem.update({
            "goal": goal,
            "completed_tasks": completed,
            "total_tasks": total,
            "progress": progress,
            "previous_plan": plan["tasks"] or mem.get("previous_plan", []),
            "weak_topics": reflection["weak_topics"],
            "previous_reflection": reflection["message"],
            "selected_tools": selected_tools
        })
        self.memory.save(mem)

        print("=== Workflow Complete ===")
        return plan
