import itertools

numberss = [[6, 10, 2], [3, 30, 34, 5, 9]]

'''시간초과'''
for numbers in numberss:
    ans = []
    nPr = list(itertools.permutations(numbers))

    for n in nPr:
        ans.append(''.join(map(str, n)))
    print(max(ans))


for numbers in numberss:
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)

    print(str(int(''.join(numbers))))



def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))