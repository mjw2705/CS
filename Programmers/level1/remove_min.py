arrs = [4, 3, 2, 1], [10]

def solution(arr):
    arr.remove(min(arr))
    if not arr:
        return [-1]
    else:
        return arr

for arr in arrs:
    print(solution(arr))