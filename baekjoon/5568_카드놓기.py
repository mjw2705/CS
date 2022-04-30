n = 4
k = 2
card_num = 1, 2, 12, 1

import itertools

num = []
card_num = list(card_num)
for n in itertools.permutations(card_num, k): 
    integ = str(n[0]) + str(n[1])
    num.append(integ)
print(set(num))
print(len(set(num)))