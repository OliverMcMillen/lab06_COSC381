import fileinput
import csv
class student:
  def __init__(self, name, studentID):
    self.name = name
    self.studentID = studentID


students_list = []

with open("Student_List.csv", mode ="r", newline = "") as file:
   reader = csv.DictReader(file)
   for row in reader:
      students_list.append({
        "Student_ID": row["Student_ID"], "Name": row["First_Name"] + " " + row["Last_Name"]
      })


#for x in students_list:
 #  print("\n", x)
