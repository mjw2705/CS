aa = [1, 2, 3, 4], [-1, 0, 1]
bb = [-3, -1, 0, 2], [1, 0, -1]

import numpy as np

for a, b in zip(aa, bb):

    ''''''
    answer = int(np.dot(a, b))
    print(answer)

    ''''''
    answer = 0
    for i, j in zip(a, b):
        answer += i * j
    print(answer)