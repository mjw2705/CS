import sys, math

x, y, w, h = map(int, sys.stdin.readline().split())

dis1 = int(math.sqrt((x-x)**2) + math.sqrt((y-h)**2))
dis2 = int(math.sqrt((x-w)**2) + math.sqrt((y-y)**2))
dis3 = int(math.sqrt((x-0)**2) + math.sqrt((y-y)**2))
dis4 = int(math.sqrt((x-x)**2) + math.sqrt((y-0)**2))

print(min(dis1, dis2, dis3, dis4))