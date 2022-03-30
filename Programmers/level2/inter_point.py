lines = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]], [[0, 1, -1], [1, 0, -1], [1, 0, 1]], [[1, -1, 0], [2, -1, 0]], [[1, -1, 0], [2, -1, 0], [4, -1, 0]]

for line in lines:

    inf = float('inf')
    minx, miny, maxx, maxy = inf, inf, -inf, -inf
    line_len = len(line)
    inter_point = []

    for i in range(line_len):
        for j in range(i + 1, line_len):
            A, B, E = line[i]
            C, D, F = line[j]
            mom = A*D - B*C
            if mom == 0:
                continue
            x = (B*F - E*D) / mom
            y = (E*C - A*F) / mom
            if x - int(x) != 0 or y - int(y) != 0:
                continue
            x, y = int(x), int(y)
            minx, miny, maxx, maxy = min(minx, x), min(miny, y), max(maxx, x), max(maxy, y)
            if [x, y] not in inter_point:
                inter_point.append([x, y])

    board = [['.' for _ in range(minx, maxx+1)] for _ in range(miny, maxy+1)]
    for x, y in inter_point:
        board[maxy-y][x-minx] = '*'
    answer = [''.join(b) for b in board]

    print(answer)