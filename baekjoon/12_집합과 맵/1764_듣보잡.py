import sys

N, M = map(int, sys.stdin.readline().split(' '))
heard = [sys.stdin.readline().strip() for _ in range(N)]
saw = [sys.stdin.readline().strip() for _ in range(M)]

intersection = list(set(heard) & set(saw))
print(len(intersection))
for inter in sorted(intersection):
    print(inter)
