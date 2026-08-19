class ProgressTool:
    """Calculate progress percentage based on completed tasks."""
    def calculate(self, completed, total):
        if total == 0:
            return 0
        return round((completed / total) * 100, 2)
