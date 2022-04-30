F = 3
friends = 'Fred Barney', 'Barney Betty', 'Betty Wilma'

def find(parents, a):
    if a == parents[a]:
        return a
    else:
        p = find(parents, parents[a])
        parents[a] = p
        return p

def union(parents, a, b, cnt):
    a = find(parents, a)
    b = find(parents, b)
    if a != b:
        parents[b] = a
        cnt[a] += cnt[b]
    print(cnt[a])

parents = {}
cnt = {}
for friend in friends:
    f1, f2 = friend.split(' ')
    if f1 not in parents:
        parents[f1] = f1
        cnt[f1] = 1
    if f2 not in parents:
        parents[f2] = f2
        cnt[f2] = 1
    union(parents, f1, f2, cnt)