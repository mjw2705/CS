numberss = [2,1,3,4,1], [5,0,2,7]

import itertools

def solution(numbers):
    answer = []
    nCr = list(itertools.combinations(numbers, 2))

    for n in nCr:
        answer.append(sum(n))
    return sorted(set(answer))

for numbers in numberss:
    print(solution(numbers))