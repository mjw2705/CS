import sys

N = int(sys.stdin.readline())
coords = list(map(int, sys.stdin.readline().strip().split(' ')))
sort_coord = sorted(coords)

n = 0
dic = {sort_coord[0]: 0}
for i in range(1, len(sort_coord)):
    if sort_coord[i] != sort_coord[i-1]:
        n += 1
    dic[sort_coord[i]] = n

for c in coords:
    print(dic[c])