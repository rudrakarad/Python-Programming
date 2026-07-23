
num = int(input("Enter a number "))
check = num
number = 0

while num > 0:
    last_digit = num % 10
    number = number * 10 + last_digit
    num //= 10

if check == number:
    print(f"The number {check} is pallindrome")
else:
    print(f"The number {check} is not palindrome")
