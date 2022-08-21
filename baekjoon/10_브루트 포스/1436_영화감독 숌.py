import sys

N = int(sys.stdin.readline())
num = 666

while N:
    if '666' in str(num):
        N -= 1
    num += 1

print(num-1)