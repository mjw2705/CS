# m = "ABCDEFG"
# musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]

# m = "ABC"
# musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]

def change(m):
    m = m.replace('C#', 'c').replace('D#','d').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    return m

def solution(m, musicinfos):
    table = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a'}

    answer = []
    # for key, value in table.items():
    #     m = m.replace(key, value)
    m = change(m)

    for musics in musicinfos:
        spl = musics.split(',')
        name = spl[2]
        code = spl[3]
        # for key, value in table.items():
        #     code = code.replace(key, value)
        code = change(code)

        s_h, s_m = list(map(int, spl[0].split(':')))
        e_h, e_m = list(map(int, spl[1].split(':')))
        time = (e_h - s_h) * 60 + e_m - s_m
        start = s_h * 60 + s_m

        melody = code * (time // len(code)) + code[:time % len(code)]

        if m in melody:
            answer.append([name, time, start])

    if not answer:
        return "(None)"
    elif len(answer) == 1:
        return answer[0][0]
    else:
        answer = sorted(answer, key=lambda x: (-x[1], x[2]))
        return answer[0][0]


print(solution(m, musicinfos))