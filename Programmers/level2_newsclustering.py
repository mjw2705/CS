import collections


str1s = ["FRANCE", "handshake", "aa1+aa2", "E=M*C^2"]
str2s = ["french", "shake hands", "AAAA12", "e=m*c^2"]

for str1, str2 in zip(str1s, str2s):
    answer = 0
    a = []
    b = []

    for st1 in range(len(str1)-1):
        s1 = str1[st1 * 1:st1 * 1 + 2]
        if s1.isalpha():
            a.append(s1.lower())

    for st2 in range(len(str2)-1):
        s2 = str2[st2 * 1:st2 * 1 + 2]
        if s2.isalpha():
            b.append(s2.lower())

    inter = set(a) & set(b)
    union = set(a) | set(b)

    inter_sum = sum([min(a.count(inter_s), b.count(inter_s)) for inter_s in inter])
    union_sum = sum([max(a.count(union_s), b.count(union_s)) for union_s in union])

    if union_sum == 0:
        answer = 65536
    else:
        answer = int((inter_sum / union_sum) * 65536)

    print(answer)

