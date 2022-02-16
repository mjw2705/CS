ns = 10, 5
import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    for num in range(2, n+1):
        if is_prime(num):
            answer += 1

    return answer

for n in ns:
    print(solution(n))