import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

ncr = list(combinations(cards, 3))
max_n = 0
for n in ncr:
    total = sum(n)
    if total >= max_n and total <= M:
        max_n = total
print(max_n)