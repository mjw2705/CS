import sys

a, b = map(int, sys.stdin.readline().split(' '))
A = set(map(int, sys.stdin.readline().split(' ')))
B = set(map(int, sys.stdin.readline().split(' ')))

# A_ = list(set(A) - set(B))
# B_ = list(set(B) - set(A))
# print(len(A_) + len(B_))

diff = list(A ^ B)
print(len(diff))
