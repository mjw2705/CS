clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

from collections import defaultdict

def solution(clothes):
    dic = defaultdict(list)
    for name, kind in clothes:
        dic[kind].append(name)

    cnt = 1
    for key in dic.keys():
        cnt *= (len(dic[key]) + 1)

    return cnt - 1