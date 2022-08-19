import itertools
import math

numberss = "17", "011"

def is_prime_number(n):
    """소수판별 함수"""
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False

        return True

for numbers in numberss:

    nCr = []
    piece = [str(i) for i in numbers]

    for i in range(1, len(piece) + 1):
        nCr += list(set(itertools.permutations(piece, i)))

    joined = [int(''.join(n)) for n in nCr]

    answer = []
    for j in set(joined):
        if is_prime_number(j):
            answer.append(j)
    print(len(answer))


def solution(numbers):
    nCr = []
    piece = [str(i) for i in numbers]

    for i in range(1, len(piece) + 1):
        nCr += list(set(itertools.permutations(piece, i)))

    joined = [int(''.join(n)) for n in nCr]

    answer = []
    for j in set(joined):
        if is_prime_number(j):
            answer.append(j)

    return len(answer)
