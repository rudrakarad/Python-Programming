

fruits = ["apple", "mango", "banana"]

with open("fruits.txt", "w")as file:
    file.write(fruits)

with open("fruits.txt", "r")as file:
    print(file.read())

except ValueError:
print("Error")