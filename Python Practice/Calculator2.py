num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
operation = input("Enter the operation to be performed")

if operation == "+":
    addition = num1 + num2
    print("The addition of the two numbers is",addition)

elif operation == "-":
    subtraction = num1 - num2
    print("The subtraction of the two numbers is",subtraction)

elif operation == "*":
    multiplication = num1 * num2
    print("The multiplication of the two numbers is",multiplication)

elif operation == "/":
    division = num1 / num2
    print("The division of the two numbers is", division)

else :
    print("Unexpected Error")