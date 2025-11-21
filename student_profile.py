from course import Course

class StudentProfile:
    """Stores all courses and computes GPA."""

    def __init__(self):
        self.courses = []

    def add_course(self, name, credits):
        self.courses.append(Course(name, credits))

    def calculate_gpa(self):
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
        """Run a what-if analysis for a future assignment."""
        course = next((c for c in self.courses if c.name == course_name), None)

        if not course:
            return None

        # Assume equal weight as average assignment weight
        if course.assignments:
            avg_weight = sum(a.weight for a in course.assignments) / len(course.assignments)
        else:
            avg_weight = 1.0  # If no assignments yet

        # Temporarily evaluate
        original_avg = course.calculate_average()
        predicted_assignment = predicted_score * avg_weight

        new_weight_sum = sum(a.weight for a in course.assignments) + avg_weight
        new_total = sum(a.get_weighted_score() for a in course.assignments) + predicted_assignment

        new_avg = new_total / new_weight_sum
        return new_avg

    def summary(self):
        lines = []
        for c in self.courses:
            avg = c.calculate_average()
            lines.append(f"{c.name}: {avg:.2f}%")
        return "\n".join(lines)