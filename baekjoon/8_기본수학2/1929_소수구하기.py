import sys, math

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

M, N = map(int, sys.stdin.readline().split())
for i in range(M, N+1):
    if is_prime(i):
        print(i)
