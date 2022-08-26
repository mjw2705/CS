import sys

num = sorted(map(str, sys.stdin.readline().strip()), reverse=True)
print(''.join(num))