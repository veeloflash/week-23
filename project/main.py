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
    parser.add_argument("--user-id", default="default")
    return parser.parse_args()


def main():
    args = parse_args()

    try:
        goal = args.goal or input("Learning goal: ").strip()
        subject = args.subject or input("Subject: ").strip()
        hours = args.hours if args.hours is not None else float(input("Weekly hours: "))
        completed = args.completed if args.completed is not None else int(input("Completed tasks: "))
        total = args.total if args.total is not None else int(input("Total tasks: "))
        user_id = args.user_id
    except ValueError as e:
        print("Invalid input: please enter valid numbers. (" + str(e) + ")")
        return 1

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

    if not isinstance(hours, (int, float)) or hours <= 0:
        print("Weekly hours must be greater than 0.")
        return 1
    if hours > 168:
        print("Weekly hours cannot exceed 168.")
        return 1
    if not isinstance(completed, int) or completed < 0:
        print("Completed tasks must be a non-negative integer.")
        return 1
    if not isinstance(total, int) or total < 0:
        print("Total tasks must be a non-negative integer.")
        return 1
    if completed > total:
        print("Completed tasks cannot exceed total tasks.")
        return 1

    try:
        LearningAgent(user_id=user_id).run(goal, subject, hours, completed, total)
    except (TypeError, ValueError, OSError) as error:
        print("Workflow error: " + str(error))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())