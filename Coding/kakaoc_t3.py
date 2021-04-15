import itertools

# numbers = [10, 40, 30, 20]
# K = 20
numbers = [3, 7, 2, 8, 6, 4, 5, 1]
K = 3


def solution(numbers, K):
    combi = list(map(list, itertools.permutations(numbers)))

    min_cnt = 99999999
    for comb in combi:
        diffs = []
        for i in range(len(comb)-1):
            diff = abs(comb[i] - comb[i+1])
            if diff > K:
                continue
            else:
                diffs.append(diff)

        cnt_swap = 0
        if len(diffs) == len(numbers) - 1:
            # print(comb)
            while numbers != comb:
                for i in range(len(numbers)):

                    if numbers[i] != comb[i]:
                        idx = numbers.index(comb[i])
                        comb[i], comb[idx] = comb[idx], comb[i]
                        # print("c: ", comb)
                        cnt_swap += 1

            if min_cnt > cnt_swap:
                min_cnt = cnt_swap

    return min_cnt


print(solution(numbers, K))

