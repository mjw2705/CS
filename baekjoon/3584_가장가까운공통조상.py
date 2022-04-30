N = 5
lines = [2, 3], [3, 4], [3, 1], [1, 5]
nodes = [3, 5]

parent = [0] * (N+1)
for line in lines:
    parent[line[1]] = line[0]

a, b = nodes[0], nodes[1]
a_parent, b_parent = [0, a], [0, b]
while parent[a]:
    a_parent.append(parent[a])
    a = parent[a]
while parent[b]:
    b_parent.append(parent[b])
    b = parent[b]

i = 1
while a_parent[-i] == b_parent[-i]:
    i += 1

print(a_parent[-i+1])