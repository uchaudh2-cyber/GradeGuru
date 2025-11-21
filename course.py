from assignment import Assignment

class Course:
    """Holds assignments and computes course averages."""

    def __init__(self, name, credits):
        self.name = name
        self.credits = int(credits)
        self.assignments = []

    def add_assignment(self, name, score, weight):
        self.assignments.append(Assignment(name, score, weight))

    def calculate_average(self):
        if not self.assignments:
            return 0.0

        total_weight = sum(a.weight for a in self.assignments)
        if total_weight == 0:
            return 0.0

        weighted_sum = sum(a.get_weighted_score() for a in self.assignments)
        return weighted_sum / total_weight

    def to_dict(self):
        return {
            "name": self.name,
            "credits": self.credits,
            "assignments": [a.to_dict() for a in self.assignments]
        }

    @staticmethod
    def from_dict(data):
        c = Course(data["name"], data["credits"])
        for a in data["assignments"]:
            c.assignments.append(Assignment.from_dict(a))
        return c

    def __repr__(self):
        return f"{self.name} ({self.credits} credits)"