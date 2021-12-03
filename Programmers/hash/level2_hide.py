clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
# clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]


type = dict()
for wear in clothes:
    if wear[1] in type.keys():
        type[wear[1]].append(wear[0])
    else:
        type[wear[1]] = [wear[0]]

result = 1
for key in type.keys():
    result = result * (len(type[key]) + 1)
print(result - 1)

# 다른 풀이
from collections import Counter
from functools import reduce

type = Counter([kind for name, kind in clothes])
answer = reduce(lambda x, y: x*(y+1), type.values(), 1) - 1
print(answer)


def solution(clothes):
    type = dict()
    for wear in clothes:
        if wear[1] in type.keys():
            type[wear[1]].append(wear[0])
        else:
            type[wear[1]] = [wear[0]]

    result = 1
    for key in type.keys():
        result = result * (len(type[key]) + 1)
    return result - 1