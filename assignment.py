class Assignment:
    """Represents one assignment with a score and weight."""

    def __init__(self, name, score, weight):
        self.name = name
        self.score = float(score)
        self.weight = float(weight)

    def get_weighted_score(self):
        """Weighted contribution to the course average."""
        return self.score * self.weight

    def to_dict(self):
        return {
            "name": self.name,
            "score": self.score,
            "weight": self.weight
        }

    @staticmethod
    def from_dict(data):
        return Assignment(data["name"], data["score"], data["weight"])

    def __repr__(self):
        return f"{self.name}: score={self.score}, weight={self.weight}"