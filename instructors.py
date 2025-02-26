import fileinput
import csv
import student
class instructors:

    def __init__(self, instructor_ID, name, course_ID, course_Name):
        self.instructor_ID = instructor_ID
        self.name = name
        self.course_ID = course_ID
        self.course_Name = course_Name

instructors_list = []


with open("Instructors.txt", 'r') as f:
    test = f.read()
    
for x in test.split("\n"):
    if x.strip():
        instructor = instructors(*x.strip().split())
        instructors_list.append(instructor)
        
for instructor in instructors_list:
    print(instructor.course_Name)
    print(instructor.course_ID)
    print(instructor.instructor_ID)
    print(instructor.name)

    
        