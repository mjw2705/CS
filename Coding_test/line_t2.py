from collections import Counter

# inp_str = "AaTa+!12-3"
# inp_str = "aaaaZZZZ)"
inp_str = "CaCbCgCdC888834A"
# inp_str = "UUUUU"
# inp_str = "ZzZz9Z824"
# inp_str = "uuuuuiiiii"


def solution(inp_str):
    result = []

    if not 8 <= len(inp_str) <= 15:
        result.append(1)

    flag2 = False
    flag3 = [0, 0, 0, 0]
    flag4 = False
    flag5 = False

    count = 0
    chr = inp_str[0]

    for str in inp_str:
        if 65 <= ord(str) <= 90:
            flag3[0] = 1
        elif 97 <= ord(str) <= 122:
            flag3[1] = 1
        elif 48 <= ord(str) <= 57:
            flag3[2] = 1
        elif str in '~!@#$%^&*':
            flag3[3] = 1
        else:
            flag2 = True

        if chr == str:
            count += 1
        else:
            count = 1
            chr = str
        if count >= 4:
            flag4 = True

    if flag2:
        result.append(2)
    if sum(flag3) < 3:
        result.append(3)
    if flag4:
        result.append(4)

    counter = Counter(inp_str)
    for v in counter.values():
        if v >= 5:
            flag5 = True
    if flag5:
        result.append(5)

    if not result:
        result.append(0)

    return result


print(solution(inp_str))