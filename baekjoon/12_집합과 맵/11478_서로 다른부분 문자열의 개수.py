import sys

s = sys.stdin.readline().strip()
arr = []
for i in range(len(s)):
    for j in range(1, len(s)+1):
        arr.append(s[i:i+j])
print(len(set(arr)))