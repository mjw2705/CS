import sys
N, k = map(int, sys.stdin.readline().split(' '))

score = sorted(map(int, sys.stdin.readline().split(' ')), reverse=True)
print(score[:k][-1])