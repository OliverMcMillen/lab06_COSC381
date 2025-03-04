import instructors
import student
import gradebook

def main():
    print("Welcome to the Gradebook System")
    instructor_id = input("Enter your instructor ID: ").strip()
    inst_course = instructors.get_instructor_by_id(instructor_id)


    if not inst_course:
        print("Instructor not found. Please check your ID.")
        return

    if len(inst_course) > 1:
        print("\nYou teach multiple courses. Please select one:")
        for idx, inst in enumerate(inst_course, 1):
            print(f"{idx}. {inst.course_Name} (Course ID: {inst.course_ID})")

        while True:
            try:
                choice = int(input("Enter the number of the course: ").strip())
                if 1 <= choice <= len(inst_course):
                    selected_course = inst_course[choice - 1]
                    break
                else:
                    print("Invalid selection. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        selected_course = inst_course[0]  # Only one course

    print(f"\nWelcome, {selected_course.name}! You are managing {selected_course.course_Name}.")

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
