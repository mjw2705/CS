ns = 3, 4
lefts = 2, 7
rights = 5, 14

import numpy as np

for n, left, right in zip(ns, lefts, rights):

    '''런타임 에러'''
    arr_2 = np.zeros((n, n), int)

    for i in range(n):
        for j in range(n):
            arr_2[i][j] = max(i, j) + 1

    arr_2 = arr_2.reshape(-1)
    print(arr_2[left:right+1].tolist())


    answer = []
    for i in range(left, right+1):
        row, col = divmod(i, n)
        answer.append(max(row, col) + 1)
    print(answer)


import numpy as np

def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        row, col = divmod(i, n)
        answer.append(max(row, col) + 1)
    return answer