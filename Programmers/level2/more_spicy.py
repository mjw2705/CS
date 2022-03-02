scoville = [1, 2, 3, 9, 10, 12]
K = 7

import numpy as np

'''정확도 100 / 효율성 0'''
def solution(scoville, K):
    cnt = 0
    scoville = np.array(scoville)
    new_scoville = scoville
    while np.any(new_scoville < K):
        if len(new_scoville) <= 1:
            return -1
        else:
            cnt += 1
            new_scoville = sorted(new_scoville)
            new = max(new_scoville[:2]) * 2 + min(new_scoville[:2])
            new_scoville = new_scoville[2:]
            new_scoville.append(new)
            new_scoville = np.array(new_scoville)
    return cnt


import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        new = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, new)
        cnt += 1
    return cnt

print(solution(scoville, K))