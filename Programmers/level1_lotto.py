lottoss = [[44, 1, 0, 0, 31, 25], [0, 0, 0, 0, 0, 0], [45, 4, 35, 20, 3, 9]]
win_numss = [[31, 10, 45, 1, 6, 19], [38, 19, 20, 40, 15, 25], [20, 9, 3, 45, 4, 35]]

for lottos, win_nums in zip(lottoss, win_numss):

    answer = []
    index = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2}
    min_rank = 0
    max_corr = 0
    for l in lottos:
        if l in win_nums:
            min_rank += 1
        if l == 0:
            max_corr += 1
    max_rank = min_rank + max_corr

    if max_rank in index.values():
        for key, value in index.items():
            if value == max_rank:
                answer.append(key)
    else:
        answer.append(6)

    if min_rank in index.values():
        for key, value in index.items():
            if value == min_rank:
                answer.append(key)
    else:
        answer.append(6)

    print(answer)


# 다른 사람 풀이
for lottos, win_nums in zip(lottoss, win_numss):

    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    answer = [rank[cnt + ans], rank[ans]]
    print(answer)
