ns = 10, 12

def solution(n):
    answer = 0
    for i in range(2, n):
        if n % i == 1:
            answer = i
            break
    return answer

for n in ns:
    print(solution(n))