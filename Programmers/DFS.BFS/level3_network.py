from re import I
from tkinter import N


ns = 3, 3
computerss = [[1, 1, 0], [1, 1, 0], [0, 0, 1]], [[1, 1, 0], [1, 1, 1], [0, 1, 1]]



for n, computers in zip(ns, computerss):

    def bfs(i):
        queue = [i]
        while queue:
            i = queue.pop(0)
            visited[i] = True
            for j in range(n):
                if computers[i][j] == 1 and not visited[j]:
                    queue.append(j)
    
    def dfs(i):
        visited[i] = True
        for j in range(n):
            if computers[i][j] and not visited[j]:
                dfs(j)

    visited = [False] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            # bfs(i)
            dfs(i)
            answer += 1

    print(answer)
