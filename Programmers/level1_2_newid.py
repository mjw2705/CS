new_ids = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", "=.=", "123_.def", "abcdefghijklmn.p"]


for new_id in new_ids:
    # 1
    new_id = new_id.lower()

    # 2
    for id in new_id:
        # 소문자
        if 97 <= ord(id) <= 122:
            pass
        # 숫자
        elif 48 <= ord(id) <= 57:
            pass
        elif id in '-_.':
            pass
        else:
            new_id = new_id.replace(id, "")

    # 3
    answer = ""
    answer += new_id[0]
    for i in range(1, len(new_id)):
        if new_id[i] == "." and new_id[i-1] == ".":
            pass
        else:
            answer += new_id[i]

    # 4
    if answer[0] == ".":
        answer = answer[1:]
    if answer and answer[-1] == ".":
        answer = answer[:-1]

    # 5
    if not answer:
        answer += "a"

    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]

    # 7
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]


# 다른 코드 참고
for new_id in new_ids:
    answer = ''
    # 1
    new_id = new_id.lower()

    # 2
    for id in new_id:
        if id.isdigit() or id.isalpha() or id in '._-':
            answer += id

    # 3
    while ".." in answer:
        answer = answer.replace("..", ".")

    # 4
    if answer[0] == ".":
        answer = answer[1:]
    if answer and answer[-1] == ".":
        answer = answer[:-1]

    # 5
    if not answer:
        answer += "a"

    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]

    # 7
    while len(answer) < 3:
        answer += answer[-1]


# 다른 사람 풀이
import re

for new_id in new_ids:
    new_id = new_id.lower()
    answer = re.sub('[^0-9a-z-_\.]', "", new_id)
    answer = re.sub('\.+', ".", answer)
    answer = re.sub('^[.]|[.]$', "", answer)
    if not answer:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        answer = re.sub('^[.]|[.]$', "", answer)
    while len(answer) < 3:
        answer += answer[-1]
    print(answer)