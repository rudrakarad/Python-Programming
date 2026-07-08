
name = input("Enter the name ")
marks = int(input("Enter the marks "))

with open("student.txt", "a") as file:
    file.write(f"{name} - {marks}\n")

with open("student.txt", "r") as file:
    print(file.read())