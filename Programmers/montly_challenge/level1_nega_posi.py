absolutess = [4,7,12], [1, 2, 3]
signss = [True, False, True], [False, False, True]


def solution(absolutes, signs):
    answer = 0
    for absolute, sign in zip(absolutes, signs):
        if sign == True:
            answer += absolute
        else:
            answer += -(absolute)
    return answer


for absolutes, signs in zip(absolutess, signss):
    print(solution(absolutes, signs))