key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


import numpy as np

def rotate_90(board):
    rotate = np.array(list(zip(*board[::-1])))
    return rotate

M, N = len(key), len(lock)
board = [[0] * (N + 2*M - 2) for _ in range(N + 2*M - 2)]

for i in range(N):
    for j in range(N):
        board[i + M - 1][j + M - 1] = lock[i][j]

rotate_key = key
answer = False
for _ in range(4):
    rotate_key = rotate_90(rotate_key)
    for i in range(N + M - 1):
        for j in range(N + M - 1):
            # key 삽입
            for k in range(M):
                for p in range(M):
                    board[i+k][j+p] += rotate_key[k][p]

            # lock과 맞는지 확인
            chk = True
            for a in range(N):
                for b in range(N):
                    if board[a + M - 1][b + M -1] != 1:
                        chk = False

            # lock과 안맞으면 key 빼기
            if not chk:
                for k in range(M):
                    for p in range(M):
                        board[i + k][j + p] -= rotate_key[k][p]
            else:
                answer = True
                break

print(answer)