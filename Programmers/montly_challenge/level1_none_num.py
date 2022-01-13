numberss = [1,2,3,4,6,7,8,0], [5,8,4,0,6,7,9]

def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer

for numbers in numberss:
    print(solution(numbers))

    
    '''다른 풀이'''
    print(45 - sum(numbers))