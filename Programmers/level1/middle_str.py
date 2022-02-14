ss = "abcde", "qwer"

for s in ss:
    length = len(s)
    if length % 2 == 0:
        answer = s[length // 2 - 1:length // 2 + 1]
    else:
        answer = s[length // 2]

    print(answer)