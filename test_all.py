from assignment import Assignment
from course import Course
from student_profile import StudentProfile
from data_manager import DataManager
import os


# -------------------------
# Assignment Tests
# -------------------------

def test_assignment_creation():
    a = Assignment("HW1", 90, 0.2)
    assert a.name == "HW1"
    assert a.score == 90
    assert a.weight == 0.2

def test_weighted_score():
    a = Assignment("Quiz", 80, 0.25)
    assert a.get_weighted_score() == 20.0

def test_assignment_to_dict():
    a = Assignment("Test", 95, 0.3)
    d = a.to_dict()
    assert d["name"] == "Test"
    assert d["score"] == 95
    assert d["weight"] == 0.3

def test_assignment_from_dict():
    d = {"name": "HW2", "score": 88, "weight": 0.2}
    a = Assignment.from_dict(d)
    assert a.name == "HW2"
    assert a.score == 88
    assert a.weight == 0.2


# -------------------------
# Course Tests
# -------------------------

def test_course_creation():
    c = Course("Math", 3)
    assert c.name == "Math"
    assert c.credits == 3
    assert len(c.assignments) == 0

def test_add_assignment():
    c = Course("Science", 4)
    c.add_assignment("Lab", 85, 0.5)
    assert len(c.assignments) == 1
    assert c.assignments[0].name == "Lab"

def test_course_average_no_assignments():
    c = Course("History", 3)
    assert c.calculate_average() == 0

def test_course_average_valid():
    c = Course("English", 3)
    c.add_assignment("Essay", 90, 0.5)
    c.add_assignment("Project", 80, 0.5)
    assert c.calculate_average() == 85


# -------------------------
# StudentProfile Tests
# -------------------------

def test_profile_add_course():
    p = StudentProfile()
    p.add_course("Math", 3)
    assert len(p.courses) == 1
    assert p.courses[0].name == "Math"

def test_gpa_no_courses():
    p = StudentProfile()
    assert p.calculate_gpa() == 0

def test_gpa_with_courses():
    p = StudentProfile()
    p.add_course("Math", 3)
    p.courses[0].add_assignment("HW", 95, 1.0)
    assert p.calculate_gpa() == 4.0

def test_what_if_course_not_found():
    p = StudentProfile()
    result = p.what_if("FakeCourse", 90)
    assert result is None

def test_what_if_prediction():
    p = StudentProfile()
    p.add_course("Science", 4)
    p.courses[0].add_assignment("Quiz", 80, 1.0)
    new_avg = p.what_if("Science", 100)
    assert new_avg > 80  


# -------------------------
# Additional StudentProfile Tests
# -------------------------

def test_letter_grade():
    p = StudentProfile()
    assert p.letter_grade(95) == "A"
    assert p.letter_grade(85) == "B"
    assert p.letter_grade(75) == "C"
    assert p.letter_grade(65) == "D"
    assert p.letter_grade(50) == "F"

def test_summary_output():
    p = StudentProfile()
    p.add_course("Math", 3)
    course = p.courses[0]

    course.add_assignment("HW", 100, 1.0)

    summary_text = p.summary()
    assert "Math: 100.00% (A)" in summary_text

# -------------------------
# DataManager Tests
# -------------------------

def test_save_and_load(tmp_path):
    filename = tmp_path / "grades.json"

    p = StudentProfile()
    p.add_course("Math", 3)
    p.courses[0].add_assignment("HW", 90, 1.0)

    DataManager.save(p, filename)
    assert os.path.exists(filename)

    loaded = DataManager.load(filename)
    assert len(loaded.courses) == 1
    assert loaded.courses[0].assignments[0].score == 90

