class Assignment:
    """Represents a single graded task for a course.

    Each assignment stores its name, raw score, and weight.
    This object makes it easy to compute how much the score
    contributes to the overall course average.
    """

    def __init__(self, name, score, weight):
        """Create a new assignment with a score and weight.

        Parameters:
            name (str): The name of the assignment.
            score (float): The score earned by the student.
            weight (float): The weight this assignment has in the course.

        All values are stored as attributes so they can be accessed
        and used by other parts of the system.
        """
        self.name = name
        self.score = float(score)
        self.weight = float(weight)

    def get_weighted_score(self):
        """Return the assignment's weighted contribution.

        This method multiplies the raw score by the weight,
        allowing the Course object to build an overall average.
        """
        return self.score * self.weight

    def to_dict(self):
        """Return a dictionary version of the assignment.

        Used when saving data to a file. This keeps the structure simple
        and compatible with JSON.
        """
        return {
            "name": self.name,
            "score": self.score,
            "weight": self.weight
        }

    @staticmethod
    def from_dict(data):
        """Re-create an Assignment object from stored dictionary data.

        This is the opposite of to_dict and helps DataManager rebuild
        the program state when loading saved work.
        """
        return Assignment(data["name"], data["score"], data["weight"])

    def __repr__(self):
        """Return a readable string showing assignment details.

        This is useful during debugging or when printing
        a course summary for the user.
        """
        return f"{self.name}: score={self.score}, weight={self.weight}"
