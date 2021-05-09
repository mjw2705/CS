info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

# 효율성 0%
def solution(info, query):
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


print(solution(info, query))