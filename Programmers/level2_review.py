"""
'''문자열 압축'''
ss = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]

for s in ss:

    def solution(s):
        answer = []
        for token in range(1, len(s) // 2):
            words = [s[i:i+token] for i in range(0, len(s), token)]

            ans = []
            cur_word = words[0]
            cnt = 1

            for a, b in zip(words, words[1:] + ['']):
                if a == b:
                    cnt += 1
                else:
                    ans.append([cur_word, cnt])
                    cur_word = b
                    cnt = 1

            length = sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in ans)
            answer.append(length)
        return min(answer)

    print(solution(s))


'''오픈채팅방'''
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]


answer = []
dic = {}
state = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
for re in record:
    spl = re.split(' ')
    if spl[0] != 'Leave':
        dic[spl[1]] = spl[2]

for re in record:
    spl = re.split(' ')
    if spl[0] != 'Change':
        answer.append(dic[spl[1]] + state[spl[0]])

print(answer)


'''메뉴 리뉴얼'''
from itertools import combinations
from collections import Counter

orderss = [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], ["XYZ", "XWY", "WXA"]]
courses = [[2, 3, 4], [2, 3, 5], [2, 3, 4]]

for orders, course in zip(orderss, courses):

    answer = []
    for cours in course:
        mapping = []
        for order in orders:
            mapping += list(map(''.join, combinations(sorted(order), cours)))

        count = Counter(mapping)

        if len(count) != 0 and max(count.values()) >= 2:
            for key in count.keys():
                if count[key] == max(count.values()):
                    answer.append(key)
    print(sorted(answer))
"""

'''괄호 변환'''
ps = ["(()())()", ")(", "()))((()"]

for p in ps:

    def is_balance(w):
        check = 0
        for w_ in w:
            if w_ == '(':
                check += 1
            else:
                check -= 1
        return not bool(check)

    def is_correct(w):
        stack = []
        for w_ in w:
            if w_ == '(':
                stack.append(w_)
            else:
                if not stack:
                    return False
                else:
                    stack.pop()
        return True

    def solution(p):
        if is_correct(p):
            return p

        for i in range(2, len(p)+1, 2):
            if is_balance(p[:i]) == True:
                u, v = p[:i], p[i:]
                break

        if is_correct(u):
            return u + solution(v)
        else:
            answer = '(' + solution(v) + ')'
            for u_ in u[1:-1]:
                if u_ == '(':
                    answer += ')'
                else:
                    answer += '('
        return answer

    print(solution(p))