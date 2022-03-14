Ns = 5, 6
roads = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
Ks = 3, 4


import sys
import heapq


def dijkstra(distance, graph):
    heap = []
    heapq.heappush(heap, (1, 0))
    while heap:
        node, cost = heapq.heappop(heap)
        if distance[node] < cost:
            continue
        for b, c in graph[node]:
            if cost + c < distance[b]:
                distance[b] = cost + c
                heapq.heappush(heap, (b, cost+ c))


def solution(N, road, K):
    INF = sys.maxsize
    # visited = [False] * (N + 1)
    distance = [INF] * (N + 1)
    distance[1] = 0

    graph = [[] for _ in range(N+1)]
    for r in road:
        a, b, c = r
        graph[a].append((b, c))
        graph[b].append((a, c)) # 양방향

    dijkstra(distance, graph)

    return len([d for d in distance if d <= K])


for N, road, K in zip(Ns, roads, Ks):
    print(solution(N, road, K))