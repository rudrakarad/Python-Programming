l = [24, 35, 46, 18, 17, 39, 67, 25]

largest = 0
while True:
    for i in l:
        if i > largest:
            largest = i
            print(largest)
            l.remove(i)