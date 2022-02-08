ns = 5, 5, 3
losts = [2, 4], [2, 4], [3]
reserves = [1, 3, 5], [3], [1]


for n, lost, reserve in zip(ns, losts, reserves):
    _reserve = set(reserve) - set(lost)
    _lost = set(lost) - set(reserve)

    for res in _reserve:
        if res - 1 in _lost:
            _lost.remove(res - 1)
        elif res + 1 in _lost:
            _lost.remove(res + 1)

    anwer = n - len(_lost)
    print(n - len(_lost))