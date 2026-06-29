num = int(input("Enter a number"))
total = 1

for i in range(1, 11):
    total = num * i
    print(num,"*",i,"=",total)