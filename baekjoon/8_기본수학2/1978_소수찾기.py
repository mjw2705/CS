import sys
import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

N = int(sys.stdin.readline())
nums = map(int, sys.stdin.readline().split())

cnt = 0
for num in nums:
    if num > 2:
        if is_prime:
            cnt += 1
print(cnt)
