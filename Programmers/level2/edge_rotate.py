rowss = 6, 3
columnss = 6, 3
queriess = [[2,2,5,4],[3,3,6,6],[5,1,6,3]], [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]


import numpy as np
for rows, columns, queries in zip(rowss, columnss, queriess):
    
    answer = []
    metrix = [[0] * columns for _ in range(rows)]
    n = 1
    for i in range(rows):
        for j in range(columns):
            metrix[i][j] = n
            n += 1
    metrix = np.array(metrix)

    for x1, y1, x2, y2 in queries:
        tmp = metrix[x1-1][y1-1]
        min_n = tmp
        for i in range(x1-1, x2-1):
            temp = metrix[i+1][y1-1]
            metrix[i][y1-1] = temp
            min_n = min(min_n, temp)

        for i in range(y1-1, y2-1):
            temp = metrix[x2-1][i+1]
            metrix[x2-1][i] = temp
            min_n = min(min_n, temp)
        for i in range(x2-1,x1-1,-1):
            temp = metrix[i-1][y2-1]
            metrix[i][y2-1] = temp
            min_n = min(min_n, temp)

        for i in range(y2-1,y1-1,-1):
            temp = metrix[x1-1][i-1]
            metrix[x1-1][i] = temp
            min_n = min(min_n, temp)
        metrix[x1-1][y1] = tmp
        answer.append(min_n)
        
    print(answer)