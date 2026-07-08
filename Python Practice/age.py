
try:
    age = int(input("Enter your age "))

except ValueError:
    print("Invalid Input")

else:
    if age < 0:
        print("The age cannot be negative")
    else:
        print(f"Your age is {age}")

finally:
    print("Thankyou")