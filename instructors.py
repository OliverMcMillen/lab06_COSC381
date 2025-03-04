import csv
import student

class Instructor:
    def __init__(self, instructor_ID, name, course_ID, course_Name):
        self.instructor_ID = instructor_ID
        self.name = name
        self.course_ID = course_ID
        self.course_Name = course_Name

# Build the list of instructors from a text file.
instructors_list = []

with open("instructors.txt", 'r') as f:
    # Expect each line to contain: instructor_ID name course_ID course_Name
    for line in f:
        if line.strip():
            parts = line.strip().split()
            if len(parts) >= 4:
                # If course name has spaces, join them:
                instructor_ID, name, course_ID = parts[0], parts[1]+" "+parts[2], parts[3]
                course_Name = " ".join(parts[4:])
                instructor = Instructor(instructor_ID, name, course_ID, course_Name)
                instructors_list.append(instructor)

print("name: " + instructor.name)

def get_instructor_by_id(instructor_ID):
    for instructor in instructors_list:
        if instructor.instructor_ID == instructor_ID:
            return instructor
    return None

# For debugging purposes.
if __name__ == "__main__":
    for inst in instructors_list:
        print(f"Course Name: {inst.course_Name}")
        print(f"Course ID: {inst.course_ID}")
        print(f"Instructor ID: {inst.instructor_ID}")
        print(f"Name: {inst.name}\n")
