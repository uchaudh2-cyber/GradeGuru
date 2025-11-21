import json
from student_profile import StudentProfile
from course import Course

class DataManager:

    @staticmethod
    def save(profile, filename="grades.json"):
        data = {"courses": [c.to_dict() for c in profile.courses]}

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load(filename="grades.json"):
        profile = StudentProfile()

        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            return profile

        for cdata in data["courses"]:
            course = Course.from_dict(cdata)
            profile.courses.append(course)

        return profile