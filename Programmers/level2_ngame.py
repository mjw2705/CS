ns = [2, 16, 16]
ts = [4, 16, 16]
ms = [2, 2, 2]
ps = [1, 1, 2]

import string

def convert(num, base):
    temp = string.digits + string.ascii_uppercase
    q, r = divmod(num, base)
    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + temp[r]

for n, t, m, p in zip(ns, ts, ms, ps):
    answer = ''
    res = ''
    for i in range(t * m):
        num = convert(i, n)
        res += num

    for idx in range(p-1, t * m, m):
        answer += res[idx]

    print(answer)
