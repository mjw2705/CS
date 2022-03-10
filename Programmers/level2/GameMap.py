maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visit = [[0] * m for _ in range(n)]

    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    queue = deque()
    queue.append([0, 0])
    visit[0][0] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[x][y] == 1:
                if visit[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append([nx, ny])
    if visit[-1][-1] <= 1:
        return -1
    return visit[-1][-1]

print(solution(maps))