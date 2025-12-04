from student_profile import StudentProfile
from data_manager import DataManager

def main():
    """Run the GradeGuru command-line interface.

    Loads existing data, displays prompts, and processes user choices.
    The program continues until the user selects Save & Exit.
    """
    profile = DataManager.load()

    while True:
        print("\n=== GradeGuru Menu ===")
        print("1. Add Course")
        print("2. Add Assignment")
        print("3. View Summary")
        print("4. Calculate GPA")
        print("5. What-If Scenario")
        print("6. Save & Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Course name: ")
            credits = input("Credits: ")
            profile.add_course(name, credits)
            print("Course added.")

        elif choice == "2":
            if not profile.courses:
                print("No courses available.")
                continue

            print("Select course:")
            for i, c in enumerate(profile.courses):
                print(f"{i+1}. {c.name}")

            idx = int(input("Course number: ")) - 1
            if idx not in range(len(profile.courses)):
                print("Invalid choice.")
                continue

            cname = input("Assignment name: ")
            score = float(input("Score: "))
            weight = float(input("Weight: "))

            profile.courses[idx].add_assignment(cname, score, weight)
            print("Assignment added.")

        elif choice == "3":
            print("\n--- Summary ---")
            print(profile.summary())

        elif choice == "4":
            gpa = profile.calculate_gpa()
            print(f"Your GPA: {gpa:.2f}")

        elif choice == "5":
            cname = input("Course name: ")
            score = float(input("Predicted future score: "))
            result = profile.what_if(cname, score)
            if result is None:
                print("Course not found.")
            else:
                print(f"What-if predicted average for {cname}: {result:.2f}%")

        elif choice == "6":
            DataManager.save(profile)
            print("Saved. Goodbye!")
            break

        else:
            print("Invalid choice.")
