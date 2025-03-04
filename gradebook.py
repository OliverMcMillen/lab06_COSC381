import csv
import os
import student
from datetime import datetime, timedelta

# Global variable for the gradebook file.
GRADEBOOK_FILE = "grades.csv"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"  # Define the date format for timestamp storage

def load_grades():
    grades = []
    if os.path.exists(GRADEBOOK_FILE):
        with open(GRADEBOOK_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                grades.append(row)
    return grades

def save_grades(grades):
    with open(GRADEBOOK_FILE, mode='w', newline='') as file:
        fieldnames = ['course_ID', 'student_ID', 'grade', 'timestamp']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for entry in grades:
            writer.writerow(entry)

def input_grade(instructor):
    grades = load_grades()
    student_id = input("Enter student ID: ").strip()
    # Check if the student exists.
    student_name = None
    for s in student.students_list:
        if s["Student_ID"] == student_id:
            student_name = s["Name"]
            break
    if student_name is None:
        print("Student not found.")
        return
    # Check if a grade already exists for this student in this course.
    for entry in grades:
        if entry["course_ID"] == instructor.course_ID and entry["student_ID"] == student_id:
            print("Grade already exists for this student in this course. Use the edit option to change it.")
            return
    grade = input(f"Enter grade for {student_name}: ").strip()
    timestamp = datetime.now().strftime(DATE_FORMAT)  # Capture the current timestamp

    grades.append({"course_ID": instructor.course_ID, "student_ID": student_id, "grade": grade, "timestamp": timestamp})
    save_grades(grades)
    print("Grade added successfully.")

def edit_grade(instructor):
    grades = load_grades()
    student_id = input("Enter student ID to edit: ").strip()
    found = False

    for entry in grades:
        if entry["course_ID"] == instructor.course_ID and entry["student_ID"] == student_id:

            original_timestamp = entry.get("timestamp", datetime.now().strftime(DATE_FORMAT))
            
            # Get the stored timestamp and convert it to datetime object
            try:
                submission_time = datetime.strptime(entry["timestamp"], DATE_FORMAT)
            except ValueError:
                print("Error: Invalid timestamp format in gradebook.")
                return

            # Check if the grade was submitted within the last 7 days
            if datetime.now() - submission_time > timedelta(days=7):
                print("This grade cannot be edited because it was first submitted more than 7 days ago.")
                return

            # Allow the instructor to edit the grade
            print(f"Current grade for student {student_id}: {entry['grade']}")
            new_grade = input("Enter new grade: ").strip()
            entry["grade"] = new_grade
            entry["timestamp"] = original_timestamp  # Update timestamp
            found = True
            break

    save_grades(grades)
    print("Grade updated successfully.")

def view_grades(instructor):
    grades = load_grades()
    print(f"\nGrades for course: {instructor.course_Name}")
    print("-" * 40)
    found_any = False
    for entry in grades:
        if entry["course_ID"] == instructor.course_ID:
            # Retrieve the student name from the student list.
            student_name = next((s["Name"] for s in student.students_list if s["Student_ID"] == entry["student_ID"]), "Unknown Student")
            print(f"Student ID: {entry['student_ID']} | Name: {student_name} | Grade: {entry['grade']} | TimeAdded: {entry['timestamp']}")
            found_any = True
    if not found_any:
        print("No grades recorded yet.")
    print("-" * 40)
