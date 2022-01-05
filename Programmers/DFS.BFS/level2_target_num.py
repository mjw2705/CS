numbers = [1, 1, 1, 1, 1]
target = 3

from itertools import product

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    products = list(map(''.join, product('+-', repeat=n)))

    for ops in products:
        val = 0
        for op, num in zip(ops, numbers):
            if op == '+':
                val += num
            else:
                val -= num
        if val == target:
            answer += 1
    return answer

print(solution(numbers, target))


'''BFS사용'''
answer = 0
n = len(numbers)
queue = [[numbers[0], 0], [-1 * numbers[0], 0]]

while queue:
    temp, idx = queue.pop()
    idx += 1

    if idx < n:
        queue.append([temp + numbers[idx], idx])
        queue.append([temp - numbers[idx], idx])
    else:
        if temp == target:
            answer += 1

print(answer)