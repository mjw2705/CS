begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

def compare(cur, word):
    cnt = 0
    for c, w in zip(cur, word):
        if c == w:
            cnt += 1
    if cnt == len(word) - 1:
        return True
    else:
        return False

def solution(begin, target, words):
    if target not in words:
        return 0

    answer = 0
    visited = [0] * len(words)
    cur_word = [begin]

    while cur_word:
        cur = cur_word.pop()
        if cur == target:
            return answer

        for i in range(len(words)):
            if not visited[i]:
                if compare(cur, words[i]):
                    visited[i] = 1
                    cur_word.append(words[i])
        answer += 1
    return 0

print(solution(begin, target, words))