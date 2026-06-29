celsius = int(input("Enter the value of celsius "))

def celsius_to_fahrenheit(celsius):
    return 9 / 5 * celsius + 32
    fahrenheit = (9 / 5 * celsius + 32)
    print("The value in fahrenheit is: ",fahrenheit)


print(celsius_to_fahrenheit(celsius))