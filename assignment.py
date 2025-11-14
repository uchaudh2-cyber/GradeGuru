# assignment.py
class Assignment:
    def __init__(self, name, score, weight):
        self.name = name
        self.score = float(score)
        self.weight = float(weight)

    def get_weighted_score(self):
        """Returns weighted contribution (score * weight)."""
        return self.score * self.weight

    def __repr__(self):
        return f"{self.name}: score={self.score}, weight={self.weight}"
