
with open("file1.txt", "w") as file:
    file.write("Python \nJava \nC++")

with open("file1.txt", "r") as file:
    copy = file.read()

with open("file2.txt", "w") as file:
    file.write(copy)

with open("file2.txt", "r") as file:
    print(file.read())

