
student_name = input("Enter the name of the student ")
student_marks = int(input("Enter the marks of the student "))

with open("student.txt", "a") as file:
    file.write(f"{student_name} - {student_marks}\n")

with open("student.txt", "r") as file:
    data = file.readlines()
    for line in data:
        print(line)

find_name = input("Enter the name to be searched ")

found = False

for line in data:
    if find_name in line:
        print("Student found successfully")
        print(line)
        found = True

if not found:
    print("Student not found")

