import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split(' ')))
m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(' ')))

dic = {}
for card in cards:
    if card in dic:
        dic[card] += 1
    else:
        dic[card] = 1

for a in arr:
    if a in dic:
        print(dic[a], end=' ')
    else:
        print('0', end=' ')