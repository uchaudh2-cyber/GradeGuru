# GradeGuru — Command-Line GPA & Grade Tracker
### Description
GradeGuru is a command-line grade calculator and GPA tracker designed to help students manage their coursework and monitor academic progress. The program allows users to add courses, record grades for individual assignments, and automatically calculate both per-course averages and overall GPA. Users can also run “what-if” scenarios to explore how future grades might affect their GPA.

The goal of this project is to demonstrate object-oriented design, file handling, and testing skills using Python.

### Requirements
Python 3.8 or higher : 

libaries:

### Project Features

Add courses and record assignments

Automatically compute weighted course averages

Calculate overall GPA based on course performance

Run “what-if” predictions for future grades

Save and load all data using JSON

Fully tested using pytest

### Project Structure
assignment.py

Defines the Assignment class.
Each assignment stores a name, score, and weight.
This class handles weighted score calculations and supports conversion to/from a dictionary for file saving.

course.py

Defines the Course class.
A course contains multiple assignments and is responsible for computing its overall weighted average.
It also supports adding assignments and converting its data for storage.

student_profile.py

Defines the StudentProfile class.
This class manages all of a student’s courses, calculates GPA, provides summaries, and runs what-if predictions.

data_manager.py

Handles saving and loading data to a JSON file.
The file is used to restore the user’s profile so progress is never lost between program runs.

menu.py

This is the main user interface.
It displays the menu options, accepts input, and calls the appropriate methods.
This is the file you run to start GradeGuru.

tests/test_all.py

Contains all pytest test functions.
These tests verify the behavior of every major part of the program, including assignments, courses, the student profile, and file storage.

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

### How to Use GradeGuru

1- Add a Course : 

2- Add asignments :

3- View currnent Course Averages : 

4- View GPA : 

5- For “What-If” Scenarios :

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
