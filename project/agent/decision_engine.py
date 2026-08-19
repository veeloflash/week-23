class DecisionEngine:
    def decide(self, progress):
        if progress < 40:
            return "intensive"
        elif progress < 80:
            return "normal"
        else:
            return "advance"
