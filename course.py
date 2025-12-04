from assignment import Assignment

class Course:
    """Represents an academic course with credits and assignments.

    A course holds several Assignment objects. Together they form
    the basis for calculating the course average and later the GPA.
    """

    def __init__(self, name, credits):
        """Create a new course with a name and credit value.

        Parameters:
            name (str): The name of the course.
            credits (int): The number of credits the course is worth.

        An empty list of assignments is created so new work
        can be added as the semester progresses.
        """
        self.name = name
        self.credits = int(credits)
        self.assignments = []

    def add_assignment(self, name, score, weight):
        """Add a new assignment to the course.

        Creates an Assignment object and stores it in the course’s
        assignment list. This follows the composition pattern
        where objects are built from other objects.
        """
        self.assignments.append(Assignment(name, score, weight))

    def calculate_average(self):
        """Return the weighted average for the course.

        If no assignments exist or weights do not add up,
        the method returns 0. This keeps the program stable
        and avoids dividing by zero.
        """
        if not self.assignments:
            return 0.0

        total_weight = sum(a.weight for a in self.assignments)
        if total_weight == 0:
            return 0.0

        weighted_sum = sum(a.get_weighted_score() for a in self.assignments)
        return weighted_sum / total_weight

    def to_dict(self):
        """Return a dictionary version of the course.

        Includes the course name, credits, and all assignments.
        This structure is used by DataManager when saving files.
        """
        return {
            "name": self.name,
            "credits": self.credits,
            "assignments": [a.to_dict() for a in self.assignments]
        }

    @staticmethod
    def from_dict(data):
        """Rebuild a Course object from stored values.

        Creates a new Course and restores each Assignment within it.
        This keeps saved data consistent when reloading.
        """
        c = Course(data["name"], data["credits"])
        for a in data["assignments"]:
            c.assignments.append(Assignment.from_dict(a))
        return c

    def __repr__(self):
        """Return a brief string showing the course name and credits.

        Helps present clean information in menus and summaries.
        """
        return f"{self.name} ({self.credits} credits)"
