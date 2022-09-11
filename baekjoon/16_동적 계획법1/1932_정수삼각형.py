import sys

n = int(sys.stdin.readline())
tri = []
for _ in range(n):
    nums = list(map(int, sys.stdin.readline().split(' ')))
    tri.append(nums)

for i in range(1, n):
    for j in range(len(tri[i])):
        if j == 0:
            tri[i][0] = tri[i-1][0] + tri[i][0]
        elif j == len(tri[i]) - 1:
            tri[i][-1] = tri[i-1][-1] + tri[i][-1]
        else:
            tri[i][j] = max(tri[i-1][j], tri[i-1][j-1]) + tri[i][j]

print(max(tri[-1]))