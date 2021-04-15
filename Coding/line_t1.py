table = ["SI JAVA JAVASCRIPT SQL PYTHON C#",
         "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
         "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
         "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]
# languages = ["PYTHON", "C++", "SQL"]
# preference = [7, 5, 5]


def solution(table, languages, preference):
    job_list = []
    int_list = [5, 4, 3, 2, 1]
    for i in table:
        score_sum = 0
        arr = i.split(" ")
        dic = dict(zip(arr[1:], int_list))

        for lang, pre in zip(languages, preference):
            if lang in dic.keys():
                score = dic.get(lang) * pre
            else:
                score = 0
            score_sum += score

        job_list.append([arr[0], score_sum])

    job_list.sort(key=lambda x: (-x[1], x[0]))
    answer = job_list[0][0]

    return answer


print(solution(table, languages, preference))


