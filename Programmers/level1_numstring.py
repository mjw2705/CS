ss = ["one4seveneight", "23four5six7", "2three45sixseven", "123"]

for s in ss:
    result = ''
    table = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
             'six':'6', 'seven': '7', 'eight': '8', 'nine': '9'}

    bag = ''
    for i in s:
        if i.isdigit():
            result += i
        else:
            bag += i
            for key, value in table.items():
                if key == bag:
                    bag = ''
                    result += value

    answer = int(result)
    print(answer)

# 다른 사람 풀이
for s in ss:
    table = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
             'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    answer = s
    for key, value in table.items():
        answer = answer.replace(key, value)
    print(int(answer))