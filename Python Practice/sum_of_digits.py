
num = int(input("Enter a number "))
total = 0

while num > 0:
    lastdigit = num % 10
    total += lastdigit
    num = num // 10

print(f"The sum is {total}")