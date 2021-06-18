# n = 6
# s = 4
# a = 6
# b = 2
# fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
n = 7
s = 3
a = 4
b = 1
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]

from math import inf
import heapq


def dijkstra(start, i):
    d = [inf] * (n+1)
    d[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])
    while heap:
        weight, node = heapq.heappop(heap)

        if d[node] < weight:
            continue

        for nod, wei in fare[node]:
            new_w = wei + weight
            if new_w < d[nod]:
                d[nod] = new_w
                heapq.heappush(heap, [new_w, nod])

    return d[i]

fare = [[] for _ in range(n+1)]

for i, j, cost in fares:
    fare[i].append([j, cost])
    fare[j].append([i, cost])

answer = inf
for i in range(1, n+1):
    answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
print(answer)


# 다른사람 풀이
# 플로이드 와샬??
def solution(n, s, a, b, fares):
    d = [ [ 20000001 for _ in range(n) ] for _ in range(n) ]
    for x in range(n):
        d[x][x] = 0
    for x, y, c in fares:
        d[x-1][y-1] = c
        d[y-1][x-1] = c

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if d[j][k] > d[j][i] + d[i][k]:
                    d[j][k] = d[j][i] + d[i][k]

    minv = 40000002
    for i in range(n):
        minv = min(minv, d[s-1][i]+d[i][a-1]+d[i][b-1])
    return minv