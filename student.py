import csv

class Student:
    def __init__(self, name, studentID):
        self.name = name
        self.studentID = studentID

# Build a list of students from the CSV.
# Expect the CSV to have headers "Student_ID", "First_Name", "Last_Name"
students_list = []
with open("student_list.csv", mode="r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        student_obj = Student(row["First_Name"] + " " + row["Last_Name"], row["Student_ID"])
        students_list.append({
            "Student_ID": student_obj.studentID,
            "Name": student_obj.name
        })

# Uncomment to check loaded students:
# for s in students_list:
#     print(s)
