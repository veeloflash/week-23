import json
import os

class MemoryManager:
    def __init__(self, path="project/memory/memory.json"):
        self.path = path
        if not os.path.exists(self.path):
            self.save({
                "goal": "",
                "completed_tasks": 0,
                "total_tasks": 0,
                "progress": 0,
                "previous_plan": [],
                "weak_topics": []
            })

    def load(self):
        try:
            with open(self.path, "r") as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError):
            data = self._default_memory()
            self.save(data)
        return data

    def save(self, data):
        os.makedirs(os.path.dirname(self.path) or ".", exist_ok=True)
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def _default_memory():
        return {
            "goal": "",
            "completed_tasks": 0,
            "total_tasks": 0,
            "progress": 0,
            "previous_plan": [],
            "weak_topics": [],
            "previous_reflection": ""
        }
