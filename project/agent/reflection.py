class ReflectionEngine:
    def reflect(self, progress, expected=60, previous_progress=None, weak_topics=None):
        if progress < expected:
            return {
                "message": "Progress is below target. Reduce workload and revisit weak topics.",
                "adjustment": "reduce_workload",
                "weak_topics": weak_topics or ["core concepts"]
            }
        if previous_progress is not None and progress <= previous_progress:
            return {
                "message": "Progress has stalled. Add targeted practice before increasing difficulty.",
                "adjustment": "targeted_practice",
                "weak_topics": weak_topics or ["recent material"]
            }
        return {
            "message": "Progress is on track. Continue and increase difficulty gradually.",
            "adjustment": "continue",
            "weak_topics": weak_topics or []
        }
