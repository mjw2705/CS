n = 8
k = 2
# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]


'''정확성 8, 효율성 0'''
def solution1(n, k, cmd):
    chart = [i for i in range(n)]
    deleted = []
    answer = ''

    for c in cmd:
        if len(c) != 1:
            direct, num = c.split(' ')
            if direct == 'D':
                k += int(num)
            else:
                k -= int(num)

            if k == len(chart):
                k -= 1

        elif c == 'C':
            deleted.append(chart[k])
            chart.pop(k)
        else:
            idx = deleted[-1]
            del deleted[-1]
            chart.insert(idx, idx)

    for i in range(n):
        if not i in chart:
            answer += 'X'
        else:
            answer += 'O'

    return answer

print(solution1(n, k, cmd))

