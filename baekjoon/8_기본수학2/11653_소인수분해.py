import sys, math

N = int(sys.stdin.readline())

# i = 2
# while N >= 2:
#     if N % i == 0:
#         print(i)
#         N //= i 
#     else:
#         i += 1

i = 2

while i <= int(math.sqrt(N)):
    if N % i == 0:
        print(i)
        N //= i 
    else:
        i += 1
if N != 1:
    print(N)