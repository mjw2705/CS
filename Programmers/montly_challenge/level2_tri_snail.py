ns = 4, 5, 6

for n in ns:

    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)]

    num = 1
    x, y = -1, 0
    for i in range(n): # 0, 1, 2, 3
        for j in range(i, n): # 0, 1, 2, 3 / 1, 2, 3 / 2, 3 / 3
            if i % 3 == 0: # 하
                x += 1
            elif i % 3 == 1: # 우
                y += 1
            else: # 상
                x -= 1
                y -= 1

            answer[x][y] = num
            num += 1
    print(answer)
    print(sum(answer, []))


def solution(n):
    answer = [[0 for j in range(1, i + 1)] for i in range(1, n + 1)]

    num = 1
    x, y = -1, 0
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:  # 하
                x += 1
            elif i % 3 == 1:  # 우
                y += 1
            else:  # 상
                x -= 1
                y -= 1

            answer[x][y] = num
            num += 1

    return sum(answer, [])