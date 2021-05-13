# grid = [[3, 4, 5], [2, 3, 4], [1, 2, 3]]
# K = 1
grid = [[2, 1, 1, 0, 1], [1, 2, 0, 3, 0], [0, 1, 5, 1, 2], [0, 0, 1, 3, 1], [1, 2, 0, 1, 1]]
K = 2

import numpy as np


def solution(grid, K):
    grid = np.array(grid)
    h, w = grid.shape
    conv_n = h - K + 1
    conv_area = [[0] * conv_n for i in range(conv_n)]

    for i in range(conv_n):
        for j in range(conv_n):
            sum_area = np.sum(grid[i:i + K, j:j + K])
            conv_area[i][j] = sum_area

    conv_area = np.array(conv_area)
    max1 = np.max(conv_area)

    max_i, max_j = map(int, np.where(conv_area == max1))
    conv_area[max_i - (K - 1):max_i + K, max_j - (K - 1):max_j + K] = 0

    max2 = np.max(conv_area)
    answer = max1 + max2

    return answer


print(solution(grid, K))