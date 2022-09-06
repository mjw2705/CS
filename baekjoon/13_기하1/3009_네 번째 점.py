import sys
from collections import Counter

x_stack = []
y_stack = []
for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    x_stack.append(x)
    y_stack.append(y)

x_cnt = Counter(x_stack)
y_cnt = Counter(y_stack)

for key, value in x_cnt.items():
    if value == 1:
        print(key, end=' ')
for key, value in y_cnt.items():
    if value == 1:
        print(key)