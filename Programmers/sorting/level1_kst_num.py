array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


answer = []
for command in commands:
    i, j, k = command
    answer.append(sorted(array[i-1:j])[k-1])
print(answer)


def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i - 1:j])[k - 1])

    return answer