# assignment.py
class Assignment:
    def __init__(self, name, score, weight):
        self.name = name
        self.score = float(score)
        self.weight = float(weight)

    def main_menu():
            print(" Student Grade Manager")
            print(" 1. Add Course")
            print(" 2. Add assignment")
            print(" 3. View Courses")
            print(" 4. Exit")

            choice = input("Select an option (1-4): ").strip()

            if choice == "1":
                print("Add Course selected")
                # TODO: add the functionality
            elif choice == "2":
                print("Add Assignment selected")
                # TODO: add the functionality
            elif choice == "3":
                print("View Courses Selected")
                # TODO: add the functionality
            elif choice == "4":
                print("Exiting program")
                # TODO: add the functionality
            else:
                print("Invalid input, please try again.")
                # TODO: loop it to select choice again
                
    
    def get_weighted_score(self):
        """Returns weighted contribution (score * weight)."""
        return self.score * self.weight

    def __repr__(self):
        return f"{self.name}: score={self.score}, weight={self.weight}"
