# 1753번 최단경로
import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
INF = sys.maxsize

graph = [[] for _ in range(V+1)]
d = [INF] * (V+1)

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])

d[start] = 0
heap = []
heapq.heappush(heap, [0, start])
while heap:
    weight, node = heapq.heappop(heap)

    for no, we in graph[node]:
        new_w = we + weight
        if new_w < d[no]:
            d[no] = new_w
            heapq.heappush(heap, [new_w, no])

for i in d[1:]:
    print(i if i != INF else "INF")

