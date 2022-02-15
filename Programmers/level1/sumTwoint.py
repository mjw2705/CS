aa = 3, 3, 5
bb = 5, 3, 3

def solution(a, b):
    if a == b:
        return a
    else:
        total = 0
        low = min(a, b)
        high = max(a, b)
        for i in range(low, high+1):
            total += i
        return total

for a, b in zip(aa, bb):
    print(solution(a, b))

    '''다른풀이'''
    if a == b:
        answer = a
    else:
        answer = sum(range(min(a, b), max(a, b) + 1))
    print(answer)