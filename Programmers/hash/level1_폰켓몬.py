numss = [3,1,2,3], [3,3,3,2,2,4], [3,3,3,2,2,2]

def solution(nums):
    get = len(nums) // 2

    kinds = len(set(nums))
    if kinds <= get:
        return kinds
    else:
        return get

for nums in numss:
    print(solution(nums))