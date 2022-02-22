nums = 3, 4

def solution(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

for num in nums:
    print(solution(num))