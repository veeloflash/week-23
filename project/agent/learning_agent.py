from project.tools.progress_tool import ProgressTool
from project.tools.study_plan_tool import StudyPlanTool
from project.tools.question_tool import QuestionTool
from project.tools.calculator_tool import CalculatorTool
from project.tools.registry import ToolRegistry
from project.agent.decision_engine import DecisionEngine
from project.agent.planner import Planner
from project.agent.reflection import ReflectionEngine
from project.memory.memory_manager import MemoryManager

class LearningAgent:
    def __init__(self, user_id="default"):
        self.user_id = user_id
        self.progress_tool = ProgressTool()
        self.study_tool = StudyPlanTool()
        self.question_tool = QuestionTool()
        self.calculator_tool = CalculatorTool()
        self.decision_engine = DecisionEngine()
        self.planner = Planner()
        self.reflection_engine = ReflectionEngine()
        self.memory = MemoryManager(user_id=user_id)
        self.registry = ToolRegistry()
        self.registry.register("progress", self.progress_tool)
        self.registry.register("study_plan", self.study_tool)
        self.registry.register("question", self.question_tool)
        self.registry.register("calculator", self.calculator_tool)

    def run(self, goal, subject, hours, completed, total):
        print("=== Learning Workflow Agent ===")

        if not isinstance(goal, str) or not goal.strip():
            raise ValueError("goal must not be empty")
        if not isinstance(subject, str) or not subject.strip():
            raise ValueError("subject must not be empty")

        mem = self.memory.load()

        progress = self.registry.execute("progress", "calculate", completed=completed, total=total)
        print("Progress: " + str(progress) + "%")

        decision = self.decision_engine.decide(progress, goal, mem)
        print("Decision: " + decision)

        selected_tools = self.decision_engine.select_tools(goal, progress, mem)
        print("Selected tools: " + ", ".join(selected_tools))

        plan_result = self.planner.plan(
            goal=goal, subject=subject, hours=hours,
            progress=progress, weak_topics=mem.get("weak_topics", []),
            decision=decision
        )
        print("Plan: " + str(plan_result["total_steps"]) + " steps")

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
                tool_errors.append("study_plan: " + str(error))

        if "question" in selected_tools:
            try:
                level = "advanced" if decision == "advance" else "beginner"
                plan["questions"] = self.registry.execute(
                    "question", "get_questions", subject=subject, level=level,
                    weak_topics=mem.get("weak_topics", [])
                )
            except (TypeError, ValueError, OSError) as error:
                tool_errors.append("question: " + str(error))

        previous_decision = mem.get("previous_decision", None)
        reflection = self.reflection_engine.reflect(
            progress,
            previous_progress=mem.get("progress"),
            weak_topics=mem.get("weak_topics", []),
            previous_decision=previous_decision
        )
        plan["selected_tools"] = selected_tools
        plan["reflection"] = reflection
        plan["plan_steps"] = plan_result["steps"]
        plan["tool_errors"] = tool_errors
        print("Reflection:", reflection["message"])

        mem.update({
            "goal": goal,
            "completed_tasks": completed,
            "total_tasks": total,
            "progress": progress,
            "previous_plan": plan.get("tasks", []) or mem.get("previous_plan", []),
            "weak_topics": reflection["weak_topics"],
            "previous_reflection": reflection["message"],
            "previous_decision": decision,
            "selected_tools": selected_tools
        })
        self.memory.save(mem)

        print("=== Workflow Complete ===")
        return plan