from collections import defaultdict, Counter

id_lists = ["muzi", "frodo", "apeach", "neo"], ["con", "ryan"]
reports = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], ["ryan con", "ryan con", "ryan con", "ryan con"]
ks = 2, 3


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic = defaultdict(list)
    stop = []

    for rep in set(report):
        key, v = rep.split(' ')
        dic[key].append(v)
        stop.append(v)

    stop_list = [ke for ke, val in Counter(stop).items() if val >= int(k)]
    
    for key, value in dic.items():
        for val in value:
            if val in stop_list:
                answer[id_list.index(key)] += 1

    return answer

for id_list, report, k in zip(id_lists, reports, ks):
    print(solution(id_list, report, k))
