import sys
from collections import Counter

g = 4
s = 11
W = 'cAda'
S = 'AbrAcadAbRa'

g, s = map(int, input().split())
W = sys.stdin.readline().strip()
S = sys.stdin.readline().strip()

wn = Counter(W)
answer = 0
for i in range(s-g+1):
    sn = Counter(S[i:i+4])
    if sn == wn:
        answer += 1
print(answer)

