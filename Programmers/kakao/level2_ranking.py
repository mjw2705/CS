info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

# 효율성 0%
def solution1(info, query):
    answer = []
    for querys in query:
        count = 0
        condition = querys.replace(" and ", " ").split(" ")

        for infos in info:
            cnt = 0
            person = infos.split(" ")

            for i in range(len(person)-1):
                if condition[i] != '-':
                    if condition[i] == person[i]:
                        cnt += 1
                else:
                    cnt += 1

            if cnt == len(person)-1:
                if int(condition[-1]) <= int(person[-1]):
                    count += 1

        answer.append(count)

    return answer


print(solution1(info, query))


from itertools import combinations

# 효율성 100%
'''이분 탐색 필요'''
def solution(info, query):
    table = {}
    answer = []

    for i in info:
        person = i.split(" ")

        condition = person[:-1]
        score = int(person[-1])

        for n in range(5):
            # print(list(combinations(condition, n)))
            for c in combinations(condition, n):
                temp = '/'.join(c)

                if temp in table:
                    table[temp].append(score)
                else:
                    table[temp] = [score]

    # score 정렬
    for value in table.values():
        value.sort()


    for q in query:
        condi = q.replace(" and ", " ").split(" ")
        q_score = int(condi[-1])
        temp = condi[:-1]
        while '-' in temp:
            temp.remove('-')
        q_query = '/'.join(temp)

        if q_query in table:
            score = table[q_query]

            if len(score) > 0:
                start, end = 0, len(score)
                while start < end:
                    mid = (start + end) // 2
                    if score[mid] >= q_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(score) - start)
        else:
            answer.append(0)

    return answer


print(solution(info, query))