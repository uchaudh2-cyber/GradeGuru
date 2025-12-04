# GradeGuru — Command-Line GPA & Grade Tracker
### Description
GradeGuru is a command-line grade calculator and GPA tracker designed to help students manage their coursework and monitor academic progress. The program allows users to add courses, record grades for individual assignments, and automatically calculate both per-course averages and overall GPA. Users can also run “what-if” scenarios to explore how future grades might affect their GPA.

The goal of this project is to demonstrate object-oriented design, file handling, and testing skills using Python.

### 📁 Requirements
- **Python 3.8 or higher**
- Standard Python libraries (no external installs required)
  
### Project Features

Add courses and record assignments

Automatically compute weighted course averages

Calculate overall GPA based on course performance

Run “what-if” predictions for future grades

Save and load all data using JSON

Fully tested using pytest

### 📚 File Descriptions

#### `assignment.py`
Defines the `Assignment` class.  
Stores:
- name  
- score  
- weight  

Handles weighted score calculations and JSON-ready dictionary conversion.

#### `course.py`
Defines the `Course` class.

Course responsibilities:
- Store multiple assignments  
- Add new assignments  
- Compute weighted course averages  
- Convert course data to/from dictionary format  

#### `student_profile.py`
Defines the `StudentProfile` class.  
Manages:
- List of courses  
- GPA calculation  
- Per-course summary  
- What-if predictions

#### `student_profile_letter.py`  
Same as `student_profile.py`, but also:
- Converts GPA values to **letter grades**  
- Useful for extended GPA reporting  

#### `data_manager.py`
Handles saving/loading data via JSON:
- Saves courses and assignments  
- Loads previous saved profiles  
- Ensures user progress is not lost  


#### `menu.py`
The main user interface.
Run this file to start **GradeGuru**.

Responsibilities:
- Display menu options  
- Get and validate user input  
- Call profile methods  
- Save data on exit
  
#### `tests/test_all.py`
Contains Pytest test cases.  
Tests:
- Assignment behavior  
- Course average calculations  
- GPA computation  
- JSON storage and retrieval
  
### How to Run the Program
1. Open a terminal inside the project folder

For example:

C:\Users\YourName\GradeGuru>

2. Run the menu program
python menu.py

3. Use the interactive menu

You will see something like:

=== GradeGuru Menu ===
1. Add Course
2. Add Assignment
3. View Summary
4. Calculate GPA
5. What-If Scenario
6. Save & Exit


You can choose:

Add Course: Creates a new course by entering a name and credit value

Add Assignment: Adds a new graded item to a course

View Summary: Shows each course and its current average

Calculate GPA: Computes your GPA based on course performance

What-If Scenario: Predicts how a future score might impact a course average

Save & Exit: Saves everything to a JSON file and closes the program

The program will guide you step by step.

### 🧮 How to Use GradeGuru
#### 1️⃣ Add a Course
- Enter course name
- Enter number of credits

#### 2️⃣ Add Assignments
- Choose a course
- Enter assignment name
- Enter score and weight

#### 3️⃣ View Course Averages
- Shows weighted average for each course.

#### 4️⃣ View Overall GPA
- Automatically calculated based on course averages + credits.

#### 5️⃣ Run “What-If” Scenarios
- Predict how a future score affects a specific course.

### Interpretation of the Output
Course Summary Example
Math: 87.50%
English: 92.00%
Biology: 78.50%


This shows you how well you are doing in each course based on weighted assignment scores.

GPA Example
Your GPA: 3.40


This value reflects your course averages weighted by credit hours.

What-If Example
What-if predicted average for Science: 85.60%


This helps you estimate how a future grade might change your course average, which can be useful for planning.

### Acknowledgements 
