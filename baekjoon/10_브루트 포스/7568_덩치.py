import sys

N = int(sys.stdin.readline())
info = []
for i in range(N):
    info.append(list(map(int, sys.stdin.readline().split(' '))))

for i in range(len(info)):
    cnt = 1
    for j in range(len(info)):
        if i == j:
            continue
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            cnt += 1
    print(cnt, end=" ")