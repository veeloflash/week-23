class ProgressTool:
    """Calculate progress percentage based on completed tasks."""
    def calculate(self, completed, total):
        if not isinstance(completed, int) or not isinstance(total, int):
            raise ValueError("completed and total tasks must be integers")
        if completed < 0 or total < 0:
            raise ValueError("task counts cannot be negative")
        if total == 0:
            return 0
        if completed > total:
            raise ValueError("completed tasks cannot exceed total tasks")
        return round((completed / total) * 100, 2)
