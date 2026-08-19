from project.tools.progress_tool import ProgressTool
from project.tools.study_plan_tool import StudyPlanTool
from project.tools.question_tool import QuestionTool
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

    def run(self, goal, subject, hours, completed, total):
        print("=== Learning Workflow Agent ===")

        # Load memory
        mem = self.memory.load()

        # Step 1: Calculate progress
        progress = self.progress_tool.calculate(completed, total)
        print(f"Progress: {progress}%")

        # Step 2: Decision
        decision = self.decision_engine.decide(progress)
        print(f"Decision: {decision}")

        # Step 3: Tool selection
        plan = self.study_tool.generate(subject, goal, hours)
        print("Generated Plan:", plan)

        # Step 4: Reflection
        reflection = self.reflection_engine.reflect(progress)
        print("Reflection:", reflection)

        # Step 5: Save memory
        mem.update({
            "goal": goal,
            "completed_tasks": completed,
            "total_tasks": total,
            "progress": progress,
            "previous_plan": plan["tasks"]
        })
        self.memory.save(mem)

        print("=== Workflow Complete ===")
        return plan
