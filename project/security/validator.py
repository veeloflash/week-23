class InputValidator:
    def validate(self, text):
        if not isinstance(text, str) or not text.strip():
            return False, "Empty input rejected."

        if len(text) > 300:
            return False, "Input too long."

        return True, ""
