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


'''뉴스 클러스터링'''
str1s = ["FRANCE", "handshake", "aa1+aa2", "E=M*C^2"]
str2s = ["french", "shake hands", "AAAA12", "e=m*c^2"]

for str1, str2 in zip(str1s, str2s):

    a, b = [], []
    str1 = str1.lower()
    str2 = str2.lower()

    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            a.append(str1[i:i+2])

    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            b.append(str2[i:i+2])

    inter = set(a) & set(b)
    union = set(a) | set(b)

    inter_s = sum([min(a.count(it), b.count(it)) for it in inter])
    union_s = sum([max(a.count(ui), b.count(ui)) for ui in union])

    if not a and not b:
        answer = 1 * 65536
    else:
        answer = int((inter_s / union_s) * 65536)
    print(answer)


'''거리두기 확인하기'''
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

from collections import deque

def bfs(p, idx):
    move_x = [1, 0, -1, 0]
    move_y = [0, -1, 0, 1]
    q = deque([idx])
    visited = [[0] * 5 for i in range(5)]

    while q:
        x, y, d = q.popleft()
        visited[x][y] = 1

        for i in range(4):
            nx = x + move_x[i]
            ny = y + move_y[i]
            nd = d + 1

            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                visited[nx][ny] = 1

                if p[nx][ny] == 'P':
                    if nd <= 2:
                        return False
                elif p[nx][ny] == 'O':
                    if nd == 1:
                        q.append([nx, ny, nd])

    return True


answer = []

for place in places:
    flag = 1

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                result = bfs(place, [i, j, 0])
                if not result:
                    flag = 0
    answer.append(flag)
print(answer)


'''수식 최대화'''
expressions = ["100-200*300-500+20", "50*6-3*2"]

import re
from itertools import permutations


for expression in expressions:

    ans = []
    oper = ['-', '+', '*']
    opers = list(permutations(oper, 3))

    p = re.compile(r'\d+|\D')
    num = p.findall(expression)

    for op in opers:
        nums = num.copy()
        for i in op:
            while i in nums:
                idx = nums.index(i)

                nums[idx-1] = str(eval(nums[idx-1] + nums[idx] + nums[idx+1]))
                nums = nums[:idx] + nums[idx+2:]
        ans.append(abs(int(nums[0])))

    answer = max(ans)
    print(answer)


'''튜플'''
ss = ["{{2},{2,1},{2,1,3},{2,1,3,4}}", "{{1,2,3},{2,1},{1,2,4,3},{2}}", "{{20,111},{111}}", "{{123}}", "{{4,2,3},{3},{2,3,4,1},{2,3}}"]

for s in ss:

    ans = []
    s = s[2:-2].split('},{')
    s = sorted(s, key=len)

    for i in s:
        num = i.split(',')

        for j in num:
            if int(j) not in ans:
                ans.append(int(j))

    print(ans)


'''순위 검색'''
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

from itertools import combinations

answer = []
db = {}
for infos in info:
    infos = infos.split(' ')
    condition = infos[:-1]
    score = int(infos[-1])

    for i in range(5):
        for combi in combinations(condition, i):
            com = '/'.join(combi)
            if com in db:
                db[com].append(score)
            else:
                db[com] = [score]

for value in db.values():
    value.sort()

for querys in query:
    querys = querys.replace(' and ', ' ').split(' ')
    condition = querys[:-1]
    q_score = int(querys[-1])

    while '-' in condition:
        condition.remove('-')
    condition = '/'.join(condition)

    if condition in db:
        score = db[condition]
        if len(score) > 0:
            start, end = 0, len(score)
            while start < end:
                mid = (start + end) // 2
                if score[mid] >= q_score:
                    end = mid
                else:
                    start = mid + 1
            answer.append(len(score) - start)
        else:
            answer.append(0)

print(answer)


'''후보키'''
relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

from itertools import combinations

n_row = len(relation)
n_col = len(relation[0])

total = []
for i in range(1, n_col + 1):
    total.extend(list(combinations(range(n_col), i)))

ans = []
for keys in total:
    tmp = [tuple(item[key] for key in keys) for item in relation]

    if len(set(tmp)) == n_row:
        ans.append(keys)

answer = set(ans)
for i in range(len(ans)):
    for j in range(i+1, len(ans)):
        c = set(ans[i]).intersection(set(ans[j]))
        if len(ans[i]) == len(set(ans[i]).intersection(set(ans[j]))):
            answer.discard(ans[j])

print(len(answer))


'''프렌즈4블록'''
ms = [4, 6]
ns = [5, 6]
boards = ["CCBDE", "AAADE", "AAABF", "CCBBF"], ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

for m, n, board in zip(ms, ns, boards):

    answer = 0
    board = list(map(list, board))

    while 1:
        remove = [[0] * n for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != 0 and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    remove[i][j], remove[i][j+1], remove[i+1][j], remove[i+1][j+1] = 1, 1, 1, 1

        cnt = 0
        for i in range(m):
            cnt += sum(remove[i])
        answer += cnt

        if cnt == 0: break

        for i in range(m-1, -1, -1):
            for j in range(n):
                if remove[i][j] == 1:
                    x = i - 1
                    while x >= 0 and remove[x][j] == 1:
                        x -= 1
                    if x < 0:
                        board[i][j] = 0
                    else:
                        board[i][j] = board[x][j]
                        remove[x][j] = 1
    print(answer)
"""


'''캐시'''
cacheSizes = [3, 3, 2, 5, 2, 0]
citiess = [["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"], ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"], \
          ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"], ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"], \
          ["Jeju", "Pangyo", "NewYork", "newyork"], ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]]

for cacheSize, cities in zip(cacheSizes, citiess):

    time = 0
    cache = []

    for city in cities:
        city = city.lower()
        if cacheSize == 0:
            time += 5
        else:
            if city in cache:
                cache.pop(cache.index(city))
                cache.append(city)
                time += 1
            else:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
                time += 5
    print(time)