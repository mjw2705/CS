import sys
from collections import Counter

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

print(round(sum(arr)/len(arr)))
print(arr[len(arr)//2])
cnt = Counter(arr).most_common(2)
if len(arr) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(arr)-min(arr))