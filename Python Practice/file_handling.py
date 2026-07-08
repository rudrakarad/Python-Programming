
with open("hello.txt", "w") as file:
    file.write("Hello, World!")

with open("hello.txt", "r") as file:
    print(file.read())

with open("hello.txt", "a") as file:
    file.write("\nWelcome to Python!")

with open("hello.txt", "r") as file:
    content = file.readlines()
    print(content)
    print(len(content))

