from collections import deque


def solution(priorities, location):
    answer = 0

    d = deque([(pri, i) for i, pri in enumerate(priorities)])
    while 1:
        item = d.popleft()

        if d and item[0] < max(d)[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break

    return answer


prioritiess = [[2, 1, 3, 2], [1, 1, 9, 1, 1, 1]]
locations = [2, 0]

for priorities, location in zip(prioritiess, locations):
    print(solution(priorities, location))