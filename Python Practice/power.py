num = int(input("Enter a number "))
expo = int(input("Enter the power "))
i = 1

def num_power(num, expo=2):  #default value of exponent is 2
    return(num ** expo)

result = num_power(num, expo)
print(f"{num} to the power of {expo} is {result}")