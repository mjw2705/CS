words = "AAAAE", "AAAE", "I", "EIO"

import itertools

def solution(word):
    dics = []
    for i in range(1, 6):
        dics += list(map(''.join, itertools.product('AEIOU', repeat=i)))
    dics = sorted(dics)
    answer = dics.index(word) + 1
    return answer

for word in words:
    print(solution(word))