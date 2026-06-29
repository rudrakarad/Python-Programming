num1 = int(input("Enter a number "))
num2 = int(input("Enter a number "))

def greatest_number(num1, num2):
    if num1 > num2:
        return(num1)
    else:
        return(num2)
    
result = greatest_number(num1, num2)
print(f"The greatest number is {result}")