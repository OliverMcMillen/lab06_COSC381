import fileinput
import csv
import student
print('Hello World')

for line in fileinput.input(files =('instructors.txt')):
    print(line)

instructors_list = []

with open("Instructors.txt", mode="r", newline="", encoding="utf-8") as txt_file:
    reader = csv.DictReader(txt_file, delimiter="\t")  # Set delimiter to tab
    
    for row in reader:
        instructors_list.append({
            "Instructor_ID": row["Instructor_ID"],
            "Instructor_Name": row["Instructor_Name"],
            "Course_ID": row["Course_ID"],
            "Course_Name": row["Course_Name"]
        })


#for x in instructors_list:
 #   print("\n", x )

    
        