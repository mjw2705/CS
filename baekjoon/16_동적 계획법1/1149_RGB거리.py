import sys

n = int(sys.stdin.readline())
costs = []
for _ in range(n):
    r, g, b = map(int, sys.stdin.readline().split(' '))
    costs.append([r, g, b])

for i in range(1, n):
    costs[i][0] = min(costs[i-1][1], costs[i-1][2]) + costs[i][0]
    costs[i][1] = min(costs[i-1][0], costs[i-1][2]) + costs[i][1]
    costs[i][2] = min(costs[i-1][0], costs[i-1][1]) + costs[i][2]

print(min(costs[-1]))