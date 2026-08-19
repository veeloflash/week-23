class InjectionDetector:
    patterns = [
        "ignore previous instructions",
        "bypass security",
        "reveal system prompt",
        "delete database"
    ]

    def detect(self, text):
        for p in self.patterns:
            if p.lower() in text.lower():
                return True, f"Injection detected: {p}"
        return False, ""
