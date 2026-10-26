class ReflectionEngine:
    def reflect(self, progress, expected=60, previous_progress=None, weak_topics=None, previous_decision=None):
        difference = progress - expected
        weak_topics = weak_topics or []

        if progress < expected:
            return {
                "message": "Progress is below target by " + str(abs(difference)) + "%. Reduce workload and revisit weak topics.",
                "adjustment": "reduce_workload",
                "expected": expected,
                "actual": progress,
                "difference": difference,
                "previous_decision": previous_decision,
                "weak_topics": weak_topics or ["core concepts"]
            }
        if previous_progress is not None and progress <= previous_progress:
            return {
                "message": "Progress has stalled. Add targeted practice before increasing difficulty.",
                "adjustment": "targeted_practice",
                "expected": expected,
                "actual": progress,
                "difference": difference,
                "previous_decision": previous_decision,
                "weak_topics": weak_topics or ["recent material"]
            }
        return {
            "message": "Progress is on track. Continue and increase difficulty gradually.",
            "adjustment": "continue",
            "expected": expected,
            "actual": progress,
            "difference": difference,
            "previous_decision": previous_decision,
            "weak_topics": []
        }