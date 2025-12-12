from student_profile import StudentProfile
from data_manager import DataManager

def get_int(prompt):
    """Ask the user for an integer until they provide one."""
    while True:
        value = input(prompt).strip()
        if value.lower() == "exit":
            return None
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid number or type 'exit' to cancel.\n")


def get_float(prompt):
    """Ask the user for a float until they provide one."""
    while True:
        value = input(prompt).strip()
        if value.lower() == "exit":
            return None
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number or type 'exit' to cancel.\n")


def get_string(prompt):
    """Ask the user for a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value.lower() == "exit":
            return None
        if value:
            return value
        print("Please enter something or type 'exit' to cancel.\n")


def main():
    profile = DataManager.load()

    print("Type 'exit' anytime to cancel an input.\n")

    while True:
        print("\n=== GradeGuru Menu ===")
        print("1. Add Course")
        print("2. Add Assignment")
        print("3. View Summary")
        print("4. Calculate GPA")
        print("5. What-If Scenario")
        print("6. Save & Exit")

        choice = get_int("Choose an option: ")
        if choice is None:
            print("Returning to menu...\n")
            continue

        # 1. Add Course
        if choice == 1:
            name = get_string("Course name: ")
            if name is None: continue

            credits = get_int("Credits: ")
            if credits is None: continue

            profile.add_course(name, credits)
            print("Course added!")

        # 2. Add Assignment
        elif choice == 2:
            if not profile.courses:
                print("No courses available. Add a course first.")
                continue

            print("\nSelect a course:")
            for i, c in enumerate(profile.courses):
                print(f"{i+1}. {c.name}")

            idx = get_int("Course number: ")
            if idx is None: continue
            idx -= 1

            if idx not in range(len(profile.courses)):
                print("Invalid course selection.")
                continue

            a_name = get_string("Assignment name: ")
            if a_name is None: continue

            score = get_float("Score: ")
            if score is None: continue

            weight = get_float("Weight: ")
            if weight is None: continue

            profile.courses[idx].add_assignment(a_name, score, weight)
            print("Assignment added!")

        # 3. View Summary
        elif choice == 3:
            print("\n--- Summary ---")
            print(profile.summary())

        # 4. Calculate GPA
        elif choice == 4:
            gpa = profile.calculate_gpa()
            print(f"Your GPA: {gpa:.2f}")

        # 5. What-If Scenario
        elif choice == 5:
            cname = get_string("Course name: ")
            if cname is None: continue

            score = get_float("Predicted score: ")
            if score is None: continue

            result = profile.what_if(cname, score)
            if result is None:
                print("Course not found.")
            else:
                print(f"What-if predicted average for {cname}: {result:.2f}%")

        # 6. Save & Exit
        elif choice == 6:
            DataManager.save(profile)
            print("Saved. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1–6.")

if __name__ == "__main__":
    main()



