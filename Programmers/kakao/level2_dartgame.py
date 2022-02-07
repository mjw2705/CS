import re

dartResults = ["1S2D*3T", "1D2S#10S", "1D2S0T", "1S*2T*3S", "1D#2S*3S",
              "1T2D3D#", "1D2S3T*"]

for dartResult in dartResults:
    answer = 0
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'*': 2, '#': -1, '': 1}

    p = re.compile('(\d+)([SDT])([*#]?)') # 왜 ?는 []밖에 위치?
    darts = p.findall(dartResult)
    # [('1', 'S', ''), ('2', 'D', '*'), ('3', 'T', '')]

    score = []
    for i in range(len(darts)):
        score.append(int(darts[i][0]) ** bonus[darts[i][1]] * option[darts[i][2]])
        if darts[i][2] == '*' and i >= 1:
            score[i-1] *= 2

    answer = sum(score)
    print(answer)