progressess = [[93, 30, 55], [95, 90, 99, 99, 80, 99], [20, 99, 93, 30, 55, 10]]
speedss= [[1, 30, 5], [1, 1, 1, 1, 1, 1], [5, 10, 1, 1, 30, 5]]

import math

for progresses, speeds in zip(progressess, speedss):

    answer = []
    cnt = 0
    distribute = [math.ceil((100 - progress) / speed) for speed, progress in zip(speeds, progresses)]

    num = distribute[0]
    for i in range(1, len(distribute)):
        if num < distribute[i]:
            cnt += 1
            answer.append(cnt)
            num = distribute[i]
            cnt = 0
        else:
            cnt += 1

    answer.append(cnt+1)
    print(answer)



import math

def solution(progresses, speeds):
    answer = []
    cnt = 0
    distribute = [math.ceil((100 - progress) / speed) for speed, progress in zip(speeds, progresses)]

    num = distribute[0]

    for i in range(1, len(distribute)):
        if num < distribute[i]:
            cnt += 1
            answer.append(cnt)
            num = distribute[i]
            cnt = 0
        else:
            cnt += 1

    answer.append(cnt + 1)

    return answer