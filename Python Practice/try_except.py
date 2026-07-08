
try:
   a = int(input("Enter 1st number "))
   b = int(input("Enter 2nd number "))

   c = a / b

   print(f"The answer is {c}")
except ZeroDivisionError:
   print("You cannot divide by 0")

except ValueError:
   print("Invalid intput")

finally:
   print("Program Ended")