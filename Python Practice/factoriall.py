num = int(input("Enter a number "))

total = 1

for i in range(num + 1):
    if i >= 1:
        total = total * i
        i -= i
print(f"The factorial of the number {num} is {total}")