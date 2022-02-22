from re import M


ns = 3, 2
ms = 12, 5

def solution(n, m):
    def GCD(n, m):
        while m:
            n, m = m, n%m
        return n
    gcd = GCD(n, m)

    def LCM(n, m):
        return n * m // gcd

    lcm = LCM(n, m)

    return [gcd, lcm]

for n, m in zip(ns, ms):
    print(solution(n, m))