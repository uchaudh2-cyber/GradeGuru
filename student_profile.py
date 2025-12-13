from course import Course

class StudentProfile:
    """
    Stores courses and handles GPA calculations.
    """

    def __init__(self):
        """Initialize empty profile."""
        self.courses = []

    def add_course(self, name, credits):
        """Add a new course."""
        self.courses.append(Course(name, credits))

    def remove_course(self, course_name):
        """Remove a course by name."""
        self.courses = [
            c for c in self.courses if c.name != course_name
        ]

    def get_course(self, course_name):
        """Return course by name or None."""
        return next((c for c in self.courses if c.name == course_name), None)

    def course_count(self):
        """Return number of courses."""
        return len(self.courses)

    def has_courses(self):
        """Return True if courses exist."""
        return len(self.courses) > 0

    def calculate_gpa(self):
        """Calculate GPA."""
        if not self.courses:
            return 0.0

        total_points = 0
        total_credits = 0

        for c in self.courses:
            avg = c.calculate_average()
            total_credits += c.credits

            if avg >= 90: points = 4.0
            elif avg >= 80: points = 3.0
            elif avg >= 70: points = 2.0
            elif avg >= 60: points = 1.0
            else: points = 0.0

            total_points += points * c.credits

        return total_points / total_credits if total_credits else 0

    def what_if(self, course_name, predicted_score):
        """Predict future average."""
        course = self.get_course(course_name)
        if not course:
            return None

        avg_weight = (
            sum(a.weight for a in course.assignments) / len(course.assignments)
            if course.assignments else 1.0
        )

        new_total = sum(a.get_weighted_score() for a in course.assignments)
        new_total += predicted_score * avg_weight
        new_weight = sum(a.weight for a in course.assignments) + avg_weight

        return new_total / new_weight

    def summary(self):
        """Return summary string."""
        return "\n".join(
            f"{c.name}: {c.calculate_average():.2f}%"
            for c in self.courses
        )

