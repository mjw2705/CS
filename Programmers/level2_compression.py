msgs = "KAKAO", "TOBEORNOTTOBEORTOBEORNOT", "ABABABABABABABAB"

'''
딕셔너리 초기화 방법
dic = dict(zip("ABCDEFGHIGKLMNOPQRSTUVWXYZ", range(1, 27)))
'''

for msg in msgs:
    dict = {}
    answer = []
    for i in range(26):
        dict[chr(65 + i)] = i + 1

    w, c = 0, 0
    while True:
        c += 1
        # KA가 없을 때, dict에 추가하고, K의 인덱스 추가
        if msg[w:c+1] not in dict:
            dict[msg[w:c+1]] = len(dict) + 1
            answer.append(dict[msg[w:c]])
            w = c
        # 마지막 글자일 때
        if c == len(msg):
            answer.append(dict[msg[w:c]])
            break

    print(answer)
