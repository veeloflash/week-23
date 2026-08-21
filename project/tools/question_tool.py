class QuestionTool:
    """Return practice questions."""
    def get_questions(self, subject, level="beginner", weak_topics=None, count=3):
        topic = weak_topics[0] if weak_topics else subject
        question_sets = {
            "beginner": [
                f"Define {topic} in your own words.",
                f"What is a simple example of {topic} in {subject}?"] ,
            "intermediate": [
                f"How would you apply {topic} to a practical {subject} problem?",
                f"What common mistake occurs when using {topic}?"] ,
            "advanced": [
                f"Compare two approaches to solving a {topic} problem in {subject}.",
                f"Design a test that distinguishes correct and incorrect use of {topic}."]
        }
        questions = question_sets.get(level, question_sets["beginner"])
        questions.append(f"Solve one {topic} exercise without looking at your notes.")
        return questions[:max(1, count)]
