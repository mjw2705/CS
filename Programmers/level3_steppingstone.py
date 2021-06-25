'''
이분 탐색 이용
'''
stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3


def solution(stones, k):
    left = 1
    right = 200000000

    while left <= right:
        mid = (left + right) // 2
        stone_copy = stones.copy()

        cnt = 0
        for stone in stone_copy:
            if stone - mid <= 0:
                cnt += 1
            else:
                cnt = 0

            # k개 이상 건너 뛸 수 없기 때문에 break
            if cnt >= k:
                break

        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1

    return left

print(solution(stones, k))