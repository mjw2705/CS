import sys

N, M = map(int, sys.stdin.readline().split(' '))
s = [sys.stdin.readline().strip() for _ in range(N)]
arr = [sys.stdin.readline().strip() for _ in range(M)]

cnt = 0 
for a in arr:
    if a in s:
        cnt += 1
print(cnt)