import sys

n = int(sys.stdin.readline())
cards = sorted(map(int, sys.stdin.readline().split(' ')))
m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(' ')))

def binary_search(arr, s, e, t):
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == t:
            return mid
        elif arr[mid] > t:
            e = mid - 1
        else:
            s = mid + 1
    return None

for a in arr:
    if binary_search(cards, 0, n-1, a) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')