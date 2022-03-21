k = 80
dungeons = 	[[80,20],[50,40],[30,10]]

from itertools import permutations

def solution(k, dungeons):
    answer = []

    npr = list(permutations(dungeons, len(dungeons)))
    for n in npr:
        cnt = 0
        n = list(n)
        nessary = k

        while nessary > 0 and n:
            ness, use = n.pop()
            if ness > nessary:
                break
            else:
                cnt += 1
                nessary -= use
        answer.append(cnt)

    return max(answer)