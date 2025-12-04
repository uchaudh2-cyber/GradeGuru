class StudentProfile:
    """Stores all courses for one student and provides GPA tools."""

    def __init__(self):
        self.courses = []

    def add_course(self, name, credits):
        self.courses.append(Course(name, credits))

    def letter_grade(self, avg):
        """Convert numeric average to letter grade."""
        if avg >= 90: return "A"
        elif avg >= 80: return "B"
        elif avg >= 70: return "C"
        elif avg >= 60: return "D"
        else: return "F"

    def calculate_gpa(self):
        if not self.courses:
            return 0.0

        total_points = 0
        total_credits = 0

        for course in self.courses:
            avg = course.calculate_average()

            if avg >= 90: points = 4.0
            elif avg >= 80: points = 3.0
            elif avg >= 70: points = 2.0
            elif avg >= 60: points = 1.0
            else: points = 0.0

            total_points += points * course.credits
            total_credits += course.credits

        return total_points / total_credits if total_credits else 0

    def summary(self):
        lines = []
        for c in self.courses:
            avg = c.calculate_average()
            grade = self.letter_grade(avg)
            lines.append(f"{c.name}: {avg:.2f}% ({grade})")
        return "\n".join(lines) 
