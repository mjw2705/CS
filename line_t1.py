import numpy as np
# table = ["SI JAVA JAVASCRIPT SQL PYTHON C#",
#          "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
#          "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
#          "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
#          "GAME C++ C# JAVASCRIPT C JAVA"]
table = ["SI JAVA JAVASCRIPT SQL PYTHON C#",
         "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
         "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
         "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]


def solution(table, languages, preference):
    scores = []
    job = []
    int_list = [5, 4, 3, 2, 1]
    job_list = []
    for i in table:
        score_sum = 0
        arr = i.split(" ")
        # job.append(arr[0])
        # del arr[0]

        dic = dict(zip(arr[1:], int_list))

        for langs, pre in zip(languages, preference):
            if langs in dic.keys():
                score = dic.get(langs) * pre
            else:
                score = 0 * pre
            score_sum += score
        # scores.append(score_sum)
        job_list.append([arr[0], score_sum])

    job_list.sort(key=lambda x: (-x[1], x[0]))
    answer = job_list[0][0]

    # diction = dict(zip(job, scores))
    # dic_max = max(diction.values())
    # jobs = []
    # for k, v in diction.items():
    #     if v == dic_max:
    #         jobs.append(k)
    # answer = sorted(jobs)[0]

    return answer

print(solution(table, languages, preference))


