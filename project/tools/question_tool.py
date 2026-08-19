class QuestionTool:
    """Return practice questions."""
    def get_questions(self, subject):
        return [
            f"What is the core concept of {subject}?",
            f"Explain one advanced idea in {subject}.",
            f"Give an example problem in {subject}."
        ]
