numbers = "1924", "1231234", "4177252841", "654321"
ks = 2, 3, 4, 5

'''시간초과'''
from itertools import combinations

for number, k in zip(numbers, ks):
    num = []
    arr = list(range(len(number)))
    nPr = list(combinations(arr, len(number) - k))
    s = ''
    for n in nPr:
        s = ''
        for i in range(len(n)):
            s += number[n[i]]
        num.append(s)
    print(max(num))


def solution(number, k):
    answer = []

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    if k != 0:
        answer = answer[:-k]

    return ''.join(answer) 

for number, k in zip(numbers, ks):
    print(solution(number, k))