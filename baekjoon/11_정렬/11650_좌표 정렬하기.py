import sys

N = int(sys.stdin.readline())
coords = []
for _ in range(N):
    coords.append(list(map(int, sys.stdin.readline().split(' '))))
# coords = sorted(coords, key=lambda x:(x[0], x[1]))
coords = sorted(coords, key=lambda x:(x[1], x[0]))
for x, y in coords:
    print(x, y)