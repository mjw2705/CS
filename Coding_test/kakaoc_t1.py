import itertools

n = 3
p = 4
c = 3


def solution(n, p, c):
    if n < 2:
        return False

    result = [0 for _ in range(n)]
    ar = [i for i in range(n)]

    arrays = list(itertools.product(ar, repeat=c))

    for i in range(n):
        count = 0
        for array in arrays:
            sum = 0
            for arr in array:
                sum += arr ** p
            if sum % n == i:
                count += 1

        result[i] = count

    temp = [i % 101 for i in result]

    return temp


print(solution(2, 3, 4))