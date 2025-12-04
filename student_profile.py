from course import Course

class StudentProfile:
    """Stores all courses for one student and provides GPA tools.

    This object manages a collection of Course objects and
    coordinates the calculations that depend on multiple courses.
    """

    def __init__(self):
        """Create a new empty student profile.

        Starts with an empty course list. Courses are added
        through menu actions or during file loading.
        """
        self.courses = []

    def add_course(self, name, credits):
        """Add a new course to the student profile.

        Creates a Course object and stores it internally.
        This supports building a full semester record.
        """
        self.courses.append(Course(name, credits))

    def calculate_gpa(self):
        """Compute the student's GPA using course averages.

        Converts numeric averages into grade points and uses
        credit values to produce a weighted GPA. Handles empty
        profiles by returning 0.
        """
        if not self.courses:
            return 0.0

        total_points = 0
        total_credits = 0

        for course in self.courses:
            avg = course.calculate_average()
            total_credits += course.credits

            if avg >= 90: points = 4.0
            elif avg >= 80: points = 3.0
            elif avg >= 70: points = 2.0
            elif avg >= 60: points = 1.0
            else: points = 0.0

            total_points += points * course.credits

        return total_points / total_credits if total_credits else 0

    def what_if(self, course_name, predicted_score):
        """Estimate a new average for a course based on a future grade.

        Finds the matching course and simulates the effect of adding
        a new assignment with an average weight. Returns None if the
        course name does not match any stored course.
        """
        course = next((c for c in self.courses if c.name == course_name), None)

        if not course:
            return None

        if course.assignments:
            avg_weight = sum(a.weight for a in course.assignments) / len(course.assignments)
        else:
            avg_weight = 1.0

        predicted_assignment = predicted_score * avg_weight
        new_weight_sum = sum(a.weight for a in course.assignments) + avg_weight
        new_total = sum(a.get_weighted_score() for a in course.assignments) + predicted_assignment

        new_avg = new_total / new_weight_sum
        return new_avg

    def summary(self):
        """Return a simple summary of each course and its average.

        Provides a clean, readable report that can be displayed
        in the menu interface.
        """
        lines = []
        for c in self.courses:
            avg = c.calculate_average()
            lines.append(f"{c.name}: {avg:.2f}%")
        return "\n".join(lines)
