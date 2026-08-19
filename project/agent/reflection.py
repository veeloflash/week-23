class ReflectionEngine:
    def reflect(self, progress, expected=60):
        if progress < expected:
            return "Previous plan was too difficult. Reduce workload."
        return "Plan is working well."
