import argparse

from security.validator import InputValidator
from security.injection_detector import InjectionDetector
from agent.learning_agent import LearningAgent

def parse_args():
    parser = argparse.ArgumentParser(description="Run the adaptive learning workflow agent.")
    parser.add_argument("--goal")
    parser.add_argument("--subject")
    parser.add_argument("--hours", type=float)
    parser.add_argument("--completed", type=int)
    parser.add_argument("--total", type=int)
    return parser.parse_args()


def main():
    args = parse_args()
    goal = args.goal or input("Learning goal: ").strip()
    subject = args.subject or input("Subject: ").strip()
    hours = args.hours if args.hours is not None else float(input("Weekly hours: "))
    completed = args.completed if args.completed is not None else int(input("Completed tasks: "))
    total = args.total if args.total is not None else int(input("Total tasks: "))

    validator = InputValidator()
    detector = InjectionDetector()
    for value in (goal, subject):
        safe, message = validator.validate(value)
        if not safe:
            print(message)
            return 1
        detected, message = detector.detect(value)
        if detected:
            print(message)
            return 1

    try:
        LearningAgent().run(goal, subject, hours, completed, total)
    except (TypeError, ValueError, OSError) as error:
        print(f"Input or workflow error: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
