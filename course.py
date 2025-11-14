# course.py
from assignment import Assignment

class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = int(credits)
        self.assignments = []

    def add_assignment(self, name, score, weight):
        """Adds a new assignment to the course."""
        new_assignment = Assignment(name, score, weight)
        self.assignments.append(new_assignment)

    def calculate_average(self):
        """Weighted course average based on all assignments."""
        if not self.assignments:
            return 0.0

        total_weight = sum(a.weight for a in self.assignments)
        if total_weight == 0:
            return 0.0

        weighted_sum = sum(a.get_weighted_score() for a in self.assignments)
        return weighted_sum / total_weight

    def __repr__(self):
        return f"{self.name} ({self.credits} credits)"
