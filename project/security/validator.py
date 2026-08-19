class InputValidator:
    def validate(self, text):
        if not text or len(text.strip()) == 0:
            return False, "Empty input rejected."

        if len(text) > 300:
            return False, "Input too long."

        return True, ""
