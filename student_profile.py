# student_profile.py
from course import Course

class StudentProfile:
    def __init__(self):
        self.courses = []

    def add_course(self, name, credits):
        new_course = Course(name, credits)
        self.courses.append(new_course)

    def calculate_gpa(self):
        """Simple GPA calculation based on course averages and credits."""
        if not self.courses:
            return 0.0

        total_points = 0
        total_credits = 0

        for course in self.courses:
            avg = course.calculate_average()
            total_credits += course.credits

            # Simple mapping: 90+=4.0, 80+=3.0, 70+=2.0, 60+=1.0, else 0
            if avg >= 90:
                points = 4.0
            elif avg >= 80:
                points = 3.0
            elif avg >= 70:
                points = 2.0
            elif avg >= 60:
                points = 1.0
            else:
                points = 0.0

            total_points += points * course.credits

        return total_points / total_credits if total_credits > 0 else 0

    def summary(self):
        """Returns a summary of all courses and averages."""
        lines = []
        for course in self.courses:
            avg = course.calculate_average()
            lines.append(f"{course.name}: {avg:.2f}%")
        return "\n".join(lines)
