import re
import unicodedata


class InjectionDetector:
    patterns = [
        "ignore previous instructions",
        "ignore all previous instructions",
        "bypass security",
        "reveal system prompt",
        "show system prompt",
        "override your instructions",
        "pretend you are the system",
        "delete database"
    ]

    def detect(self, text):
        normalized = unicodedata.normalize("NFKC", text).lower()
        normalized = re.sub(r"\s+", " ", normalized).strip()
        for p in self.patterns:
            if p in normalized:
                return True, f"Injection detected: {p}"
        return False, ""
