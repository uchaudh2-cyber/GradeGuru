# data_manager.py
import json

class DataManager:
    """Handles saving and loading data to a JSON file."""

    @staticmethod
    def save(profile, filename="grades.json"):
        data = {
            "courses": []
        }

        for course in profile.courses:
            course_data = {
                "name": course.name,
                "credits": course.credits,
                "assignments": [
                    {"name": a.name, "score": a.score, "weight": a.weight}
                    for a in course.assignments
                ]
            }
            data["courses"].append(course_data)

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load(filename="grades.json"):
        from student_profile import StudentProfile
        from course import Course
        from assignment import Assignment

        profile = StudentProfile()

        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            return profile  # empty profile

        for c in data.get("courses", []):
            course = Course(c["name"], c["credits"])
            for a in c["assignments"]:
                assignment = Assignment(a["name"], a["score"], a["weight"])
                course.assignments.append(assignment)

            profile.courses.append(course)

        return profile
