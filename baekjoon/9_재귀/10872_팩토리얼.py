import sys

def factorial(num):
    result = 1
    if num >= 1:
        result = num * factorial(num-1)
    return result

N = int(sys.stdin.readline())
print(factorial(N))


from math import factorial
N = int(sys.stdin.readline())
print(factorial(N))