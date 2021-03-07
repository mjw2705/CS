import sys


# 2606번 바이러스
def DFS_2606():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    dic = {}
    for i in range(n):
        dic[i + 1] = set()

    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        dic[a].add(b)
        dic[b].add(a)

    def dfs(start, dic):
        for i in dic[start]:
            if i not in visit:
                visit.append(i)
                dfs(i, dic)

    def bfs(start, dic):
        queue = [start]
        while queue:
            for i in dic[queue.pop()]:
                if i not in visit:
                    visit.append(i)
                    queue.append(i)

    visit = []
    dfs(1, dic)
    print(len(visit) - 1)


# 2178번 미로탐색
def BFS_2178():
    height, width = map(int, sys.stdin.readline().split())
    matrix = [sys.stdin.readline().rstrip() for _ in range(height)]

    visit = [[0] * width for _ in range(height)]
    #좌우위아래
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    visit[0][0] = 1
    queue = [(0, 0)]

    while queue:
        x, y = queue.pop(0)

        if x == height-1 and y == width-1:
            print(visit[x][y])
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < height and 0 <= ny < width:
                if visit[nx][ny] == 0 and matrix[nx][ny] == '1':
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append((nx, ny))


if __name__ == '__main__':
    # DFS_2606()
    BFS_2178()