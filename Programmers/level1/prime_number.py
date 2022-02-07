import itertools, math

numss = [1, 2, 3, 4], [1, 2, 7, 6, 4]

def is_prime_num(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    nCr = list(itertools.combinations(nums, 3))
    answer = 0
    for n in nCr:
        total = sum(n)

        if is_prime_num(total):
            answer += 1

    return answer


for nums in numss:
    print(solution(nums))