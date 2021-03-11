import sys
import heapq

# 11725번 트리의 부모 찾기
def Tree_11725():
    N = int(sys.stdin.readline())
    tree = [[] for _ in range(N+1)]
    parents = [[] for _ in range(N+1)]

    for _ in range(N-1):
        i, j = map(int, sys.stdin.readline().split())
        tree[j].append(i)
        tree[i].append(j)

    def DFS(tree, start, parents):
        stack = [start]

        while stack:
            node = stack.pop()
            for i in tree[node]:
                parents[i].append(node)
                stack.append(i)
                tree[i].remove(node)

    DFS(tree, 1, parents)
    for i in parents[2:]:
        print(i[0])


# 1967번 트리의 지름
def Tree_1967():
    INF = sys.maxsize
    n = int(sys.stdin.readline())
    tree = [[] for _ in range(n+1)]
    d = [INF] * (n+1)
    for _ in range(n-1):
        p, c, w = map(int, sys.stdin.readline().split())
        tree[p].append([c, w])
        tree[c].append([p, w])

    def dijkstra(start):
        d = [INF] * (n + 1)
        d[start] = 0
        heap = []
        heapq.heappush(heap, [0, start])
        while heap:
            weight, node = heapq.heappop(heap)

            for no, we in tree[node]:
                new_w = we + weight
                if new_w < d[no]:
                    d[no] = new_w
                    heapq.heappush(heap, [new_w, no])

        return d

    max_index = dijkstra(1)
    mmax = dijkstra(max_index.index(max(max_index[1:])))
    print(max(mmax[1:]))


# 1991번 트리 순회



# if __name__ == '__main__':
    # Tree_11725()
    # Tree_1967()