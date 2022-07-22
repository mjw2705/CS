import sys

def fibo(num):
    if num <= 1:
        return num
    return fibo(num-1) + fibo(num-2)

N = int(sys.stdin.readline())
print(fibo(N))