import json
from student_profile import StudentProfile
from course import Course

class DataManager:
    """Handles saving and loading student grade data.

    Uses JSON so course and assignment information can be stored
    between runs. This relies on basic file I/O concepts.
    """

    @staticmethod
    def save(profile, filename="grades.json"):
        """Save the student profile to a JSON file.

        Converts all course and assignment objects into dictionaries
        so the data can be easily written as text. The file is opened
        in write mode and closed automatically.
        """
        data = {"courses": [c.to_dict() for c in profile.courses]}

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load(filename="grades.json"):
        """Load saved grade data from a JSON file.

        If the file is missing, an empty StudentProfile is returned.
        Otherwise, the method rebuilds all Course and Assignment
        objects so the user can continue where they left off.
        """
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
