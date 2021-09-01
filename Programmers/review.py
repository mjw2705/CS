"""
'''로또'''
lottoss = [[44, 1, 0, 0, 31, 25], [0, 0, 0, 0, 0, 0], [45, 4, 35, 20, 3, 9]]
win_numss = [[31, 10, 45, 1, 6, 19], [38, 19, 20, 40, 15, 25], [20, 9, 3, 45, 4, 35]]

for lottos, win_nums in zip(lottoss, win_numss):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt_0 = lottos.count(0)
    min_cnt = 0
    for num in win_nums:
        if num in lottos:
            min_cnt += 1
    max_cnt = cnt_0 + min_cnt

    answer = [rank[max_cnt], rank[min_cnt]]


'''신규 아이디'''
import re
new_ids = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", "=.=",
           "123_.def", "abcdefghijklmn.p"]

for new_id in new_ids:
    new_id = new_id.lower()
    new_id = re.sub(r'[^\w\-\_\.]', '', new_id)
    new_id = re.sub(r'\.+', '.', new_id)
    new_id = re.sub(r'^\.|\.$', '', new_id)
    if not new_id:
        new_id += 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = re.sub(r'^[.]|[.]$', '', new_id)
    elif len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]


'''숫자문자열과 영단어'''
alpha = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
         6:'six', 7:'seven', 8:'eight', 9:'nine'}

ss = ["one4seveneight", "23four5six7", "2three45sixseven", "123"]
for s in ss:
    for key, value in alpha.items():
        s = s.replace(value, str(key))
    answer = int(s)


'''키패드 누르기'''
import numpy as np

numberss = [[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]
hands = ['right', 'left', 'right']

for numbers, hand in zip(numberss, hands):
    keypad = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']])
    left_loc = '*'
    right_loc = '#'
    result = ""
    for num in numbers:
        if num in [1, 4, 7]:
            result += 'L'
        elif num in [3, 6, 9]:
            result += 'R'
        else:
            loc_i, loc_j = np.where(keypad==str(num))
            left_i, left_j = np.where(keypad==str(left_loc))
            right_i, right_j = np.where(keypad==str(right_loc))

            left_dis = abs(left_i-loc_i) + abs(left_j-loc_j)
            right_dis = abs(right_i-loc_i) + abs(right_j-loc_j)

            if left_dis == right_dis:
                if hand == 'right':
                    result += 'R'
                else:
                    result += 'L'
            elif left_dis > right_dis:
                result += 'R'
            else:
                result += 'L'

        if result[-1] == 'L':
            left_loc = num
        else:
            right_loc = num

    print(result)
"""

