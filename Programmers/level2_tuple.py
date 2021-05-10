import re
from collections import Counter

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
# s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
# s = "{{123}}"


def solution(s):
    answer = []
    tuple = s[2:-2].split("},{")
    tuple = sorted(tuple, key=len)

    for i in tuple:
        k = i.split(',')
        for j in k:
            if int(j) not in answer:
                answer.append(int(j))

    return answer


print(solution(s))

