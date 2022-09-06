import sys
import math

r = int(sys.stdin.readline())
euclid = r ** 2 * math.pi
taxi = 2 * r ** 2
print(f'{euclid:.6f}')
print(f'{taxi:.6f}')