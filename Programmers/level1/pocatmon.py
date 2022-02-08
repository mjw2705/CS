numss = [3,1,2,3], [3,3,3,2,2,4], [3,3,3,2,2,2]


def solution(nums):
    get = len(nums) // 2
    sets = len(set(nums))
    
    if sets <= get:
        return sets
    else:
        return get

for nums in numss:
    print(solution(nums))