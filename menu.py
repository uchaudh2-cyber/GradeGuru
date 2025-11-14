# menu.py (main application)
from student_profile import StudentProfile
from data_manager import DataManager

def main():
    profile = DataManager.load()

    while True:
        print("\n=== GradeGuru Menu ===")
        print("1. Add Course")
        print("2. Add Assignment to Course")
        print("3. View Summary")
        print("4. Calculate GPA")
        print("5. Save and Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Course name: ")
            credits = input("Credits: ")
            profile.add_course(name, credits)
            print("Course added.")

        elif choice == "2":
            if not profile.courses:
                print("No courses yet.")
                continue

            print("Select a course:")
            for i, c in enumerate(profile.courses):
                print(f"{i+1}. {c.name}")

            idx = int(input("Course number: ")) - 1

            if 0 <= idx < len(profile.courses):
                cname = input("Assignment name: ")
                score = input("Score: ")
                weight = input("Weight: ")
                profile.courses[idx].add_assignment(cname, score, weight)
                print("Assignment added.")
            else:
                print("Invalid selection.")

        elif choice == "3":
            print("\n--- Course Summary ---")
            print(profile.summary())

        elif choice == "4":
            gpa = profile.calculate_gpa()
            print(f"Your GPA: {gpa:.2f}")

        elif choice == "5":
            DataManager.save(profile)
            print("Saved. Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
