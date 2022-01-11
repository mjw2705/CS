lefts = 13, 24
rights = 17, 27

def solution(left, right):
    answer = 0

    for num in range(left, right+1):
        cnt = 0
        for i in range(1, num+1):
            if num % i == 0:
                cnt += 1

        if cnt % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer

for left, right in zip(lefts, rights):
    print(solution(left, right))



'''제곱근 사용(시간복잡도 : O(logn)'''
import math
for left, right in zip(lefts, rights):

    answer = 0
    for num in range(left, right + 1):
        cnt = 0
        sqrt = math.sqrt(num)

        for i in range(1, int(sqrt) + 1):
            if num % i == 0:
                if (num // i) != i:
                    cnt += 1
                cnt += 1

        if cnt % 2 == 0:
            answer += num
        else:
            answer -= num

    print(answer)
