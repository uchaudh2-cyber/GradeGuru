class Assignment:
    """
    Represents a single graded task for a course.
    Stores name, score, and weight.
    """

    def __init__(self, name, score, weight):
        """Initialize an assignment."""
        self.name = name
        self.score = float(score)
        self.weight = float(weight)

    def get_weighted_score(self):
        """Return weighted score contribution."""
        return self.score * self.weight

    def update_score(self, new_score):
        """Update the assignment score."""
        self.score = float(new_score)

    def update_weight(self, new_weight):
        """Update the assignment weight."""
        self.weight = float(new_weight)

    def is_passing(self):
        """Return True if score is passing (>= 60)."""
        return self.score >= 60

    def to_dict(self):
        """Convert assignment to dictionary."""
        return {
            "name": self.name,
            "score": self.score,
            "weight": self.weight
        }

    @staticmethod
    def from_dict(data):
        """Create Assignment from dictionary."""
        return Assignment(data["name"], data["score"], data["weight"])

    def __repr__(self):
        """Readable representation of assignment."""
        return f"{self.name}: score={self.score}, weight={self.weight}"

