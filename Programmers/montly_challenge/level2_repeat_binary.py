ss = "110010101001", "01110", "1111111"


def solution(s):
    cnt_zero = 0
    cnt = 0

    while s != '1':
        if '0' in s:
            cnt_zero += s.count('0')
            s = s.replace('0', '')
        s = bin(len(s))[2:]
        cnt += 1

    answer = [cnt, cnt_zero]
    return answer


for s in ss:
    print(solution(s))