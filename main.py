import instructors
import student
import gradebook

def main():
    print("Welcome to the Gradebook System")
    instructor_id = input("Enter your instructor ID: ").strip()
    inst = instructors.get_instructor_by_id(instructor_id)
    if not inst:
        print("Instructor not found. Please check your ID.")
        return

    print(f"Welcome, {inst.name}!")
    while True:
        print("\nPlease select an option:")
        print("1. Input student grade")
        print("2. Edit student grade")
        print("3. View student grades")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            gradebook.input_grade(inst)
        elif choice == "2":
            gradebook.edit_grade(inst)
        elif choice == "3":
            gradebook.view_grades(inst)
        elif choice == "4":
            print("Exiting the Gradebook System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
