arr = 10, 12, 11, 13

for x in arr:
    n = sum(map(int, str(x)))
    if x % n == 0:
        print(True)
    else:
        print(False)