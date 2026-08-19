from project.security.validator import InputValidator
from project.security.injection_detector import InjectionDetector
from project.agent.learning_agent import LearningAgent

validator = InputValidator()
detector = InjectionDetector()
agent = LearningAgent()

user_goal = "Finish Python basics in 4 weeks"
subject = "python"
hours = 7
completed = 4
total = 10

# Security
safe, msg = validator.validate(user_goal)
if not safe:
    print(msg)
    exit()

inj, msg = detector.detect(user_goal)
if inj:
    print(msg)
    exit()

# Run agent
agent.run(user_goal, subject, hours, completed, total)
