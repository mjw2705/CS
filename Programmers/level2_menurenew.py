from collections import Counter
from itertools import combinations

# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2, 3, 4]
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2, 3, 5]


def solution(orders, course):
    answer = []

    for c in course:
        combi = []
        for order in orders:
            combi += combinations(sorted(order), c)

        count = Counter(combi)

        if len(count) != 0 and max(count.values()) >= 2:
            for coun in count:
                if count[coun] == max(count.values()):
                    answer.append(''.join(coun))

    answer = sorted(answer)

    return answer


print(solution(orders, course))
