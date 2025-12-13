from assignment import Assignment

class Course:
    """
    Represents an academic course with assignments and credits.
    """

    def __init__(self, name, credits):
        """Initialize course."""
        self.name = name
        self.credits = int(credits)
        self.assignments = []

    def add_assignment(self, name, score, weight):
        """Add an assignment."""
        self.assignments.append(Assignment(name, score, weight))

    def remove_assignment(self, assignment_name):
        """Remove assignment by name."""
        self.assignments = [
            a for a in self.assignments if a.name != assignment_name
        ]

    def has_assignments(self):
        """Return True if course has assignments."""
        return len(self.assignments) > 0

    def assignment_count(self):
        """Return number of assignments."""
        return len(self.assignments)

    def calculate_average(self):
        """Return weighted course average."""
        if not self.assignments:
            return 0.0
        total_weight = sum(a.weight for a in self.assignments)
        if total_weight == 0:
            return 0.0
        return sum(a.get_weighted_score() for a in self.assignments) / total_weight

    def to_dict(self):
        """Convert course to dictionary."""
        return {
            "name": self.name,
            "credits": self.credits,
            "assignments": [a.to_dict() for a in self.assignments]
        }

    @staticmethod
    def from_dict(data):
        """Create Course from dictionary."""
        c = Course(data["name"], data["credits"])
        for a in data["assignments"]:
            c.assignments.append(Assignment.from_dict(a))
        return c

    def __repr__(self):
        """Readable representation."""
        return f"{self.name} ({self.credits} credits)"



