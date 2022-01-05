ns = 45, 125

for n in ns:

    three = ''
    while n > 0:
        n, b = divmod(n, 3)
        three += str(b)

    answer = int(three, 3)
    print(answer)