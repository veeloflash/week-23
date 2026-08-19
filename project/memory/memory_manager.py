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
        with open(self.path, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)
