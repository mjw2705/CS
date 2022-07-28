array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        part_arr = sorted(array[i-1:j])
        answer.append(part_arr[k-1])
    return answer

part = list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
print(part)