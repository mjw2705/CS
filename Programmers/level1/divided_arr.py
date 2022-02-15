arrs = [5, 9, 7, 10], [2, 36, 1, 3], [3,2,6]
divisors = 5, 1, 10

for arr, divisor in zip(arrs, divisors):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    
    if not answer:
        answer = [-1]

    print(sorted(answer))