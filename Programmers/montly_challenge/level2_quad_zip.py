import numpy as np

arrs = [[0, 0], [0, 0]], [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]], [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]


def solution(arr):
    def fn(a):
        n = len(a) // 2

        if np.all(a == 0):
            return np.array([1, 0])
        elif np.all(a == 1):
            return np.array([0, 1])
        else:
            return fn(a[:n, :n]) + fn(a[n:, :n]) + fn(a[:n, n:]) + fn(a[n:, n:])
    return fn(np.array(arr)).tolist()