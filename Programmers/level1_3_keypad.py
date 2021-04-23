# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = "right"
# numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# hand = "left"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"

import numpy as np

keypad = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']])

answer = ''
location_r = '*'
location_l = '#'
for number in numbers:
    if number == 1 or number == 4 or number == 7:
        answer += 'L'
        location_l = number
    elif number == 3 or number == 6 or number == 9:
        answer += 'R'
        location_r = number
    else:
        num_i, num_j = np.where(keypad == str(number))

        l_i, l_j = np.where(keypad == str(location_l))
        r_i, r_j = np.where(keypad == str(location_r))

        dis_l = abs(num_i - l_i) + abs(num_j - l_j)
        dis_r = abs(num_i - r_i) + abs(num_j - r_j)

        if dis_r > dis_l:
            answer += 'L'
            location_l = number
        elif dis_r < dis_l:
            answer += 'R'
            location_r = number
        else:
            if hand == 'right':
                answer += 'R'
                location_r = number
            else:
                answer += 'L'
                location_l = number


print(answer)


