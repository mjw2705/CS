n = 7
m = 8
calc = [0, 1, 3], [1, 1, 7], [0, 7, 6], [1, 7, 1], [0, 3, 7], [0, 4, 2], [0, 1, 1], [1, 1, 1]

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

def find(a):
    if a == parent[a]:
        return a
    else:
        p = find(parent[a])
        return p

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for c in calc:
    if c[0] == 0:
        union(c[1], c[2])
        print(parent)
    else:
        if find(c[1]) == find(c[2]):
            print('Yes')
        else:
            print('No')
