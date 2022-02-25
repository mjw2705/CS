xs = 2, 4, -4
ns = 5, 3, 2

for x, n in zip(xs, ns):

    answer = []
    for i in range(n):
        answer.append(x + x*i)
    print(answer)

    print(list(range(x, x * (n+1), x)))
