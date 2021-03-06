# 9184번 신나는 함수 실행
def dynamic_9184():
    def w(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return 1
        elif a > 20 or b > 20 or c > 20:
            return w(20, 20, 20)

        if dp[a][b][c] != 0:
            return dp[a][b][c]

        if a < b < c:
            dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        else:
            dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

        return dp[a][b][c]

    dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
    while True:
        a, b, c = map(int, input().split())
        if a == -1 and b == -1 and c == -1:
            break
        print(f'w({a}, {b}, {c}) = {w(a, b, c)}')


# 1932번 정수 삼각형
def dynamic_1932():
    size = int(input())
    tri = []
    for _ in range(size):
        tri.append(list(map(int, input().split())))

    sum = []
    for i in range(1, size + 1):
        sum.append([0 for _ in range(i)])

    for i in range(size):
        if i == 0:
            sum[0][0] = tri[0][0]
        else:
            for j in range(i + 1):
                if j == 0:
                    sum[i][j] = sum[i-1][j] + tri[i][j]
                elif j == i:
                    sum[i][j] = sum[i-1][j-1] + tri[i][j]
                else:
                    sum[i][j] = max(sum[i-1][j-1] + tri[i][j], sum[i-1][j] + tri[i][j])

    print(max(sum[-1]))


# 2565번 전깃줄
def dynamic_2565():
    size = int(input())
    line = [list(map(int, input().split())) for _ in range(size)]

    sort_line = sorted(line, key=lambda x: x[0])
    lis = [0 for _ in range(size)]

    for i in range(size):
        min_value = 0
        for j in range(i):
            if sort_line[i][1] > sort_line[j][1]:
                min_value = max(lis[j], min_value)
        lis[i] = min_value + 1

    print(size - max(lis))


if __name__ == '__main__':
    # dynamic_9184()
    # dynamic_1932()
    dynamic_2565()