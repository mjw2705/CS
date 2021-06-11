# board = [[0,0,0],[0,0,0],[0,0,0]]
# [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
# board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]

import math


# 런타임 에러
def solution(board):
    N = len(board)
    visit = [[[math.inf] * 4 for _ in range(N)] for _ in range(N)]

    # 상, 하, 좌, 우 (0, 1, 2, 3)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = [(0, 0, -1)] # x, y, 방향
    visit[0][0] = [0, 0, 0, 0]

    while queue:
        x, y, direct = queue.pop(0)

        for i in range(4):
            if abs(i - direct) == 1: # 다시 반대로 돌아가는 경우 pass
                continue
            nx = x + dx[i]
            ny = y + dy[i]
            cost = 100

            if i != direct and direct != -1:
                cost += 500

            # 저장되있는 값보다 작으면 update
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0 and visit[nx][ny][i] > cost + visit[x][y][direct]:
                visit[nx][ny][i] = cost + visit[x][y][direct]
                queue.append([nx, ny, i])
    answer = min(visit[N-1][N-1])

    return answer


