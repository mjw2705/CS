import sys

inputs = []
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0:
        break
    inputs.append(sorted([a, b, c]))

for a, b, c in inputs:
    if c ** 2 == a **2 + b **2:
        print("right")
    else:
        print("wrong")