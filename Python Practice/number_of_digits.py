
num = int(input("Enter a number "))
total = 0

while num > 0:
    num % 10
    total += 1
    num //= 10

print(f"The number of digits are {total}")