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
"""

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