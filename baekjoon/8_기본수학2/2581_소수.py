import sys
import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

prime = []
for num in range(M, N+1):
    if num == 1:
        continue
    if is_prime(num):
        prime.append(num)

if not prime:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])

