# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
# N = 4
# stages = [4,4,4,4,4]
N = 5
stages = [2,1,2,4,2,4,3,3]


# people이 0이 되는 경우의 예외 처리 필요
def solution(N, stages):
    missrate = []
    stage = [i for i in range(1, N + 1)]

    for i in stage:
        miss = 0
        people = 0
        for j in stages:
            if j >= i:
                people += 1
                if j <= i:
                    miss += 1
        if people != 0:
            missrate.append(miss / people)
        else:
            missrate.append(0)

    dic = dict(zip(stage, missrate))
    dic_sort = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    answer = [i[0] for i in dic_sort]

    return answer


print(solution(N, stages))