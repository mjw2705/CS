ns = 3, 5, 2
wordss = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"], ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"], ["hello", "one", "even", "never", "now", "world", "draw"]

def solution(n, words):
    save = [words[0]]
    nums = [0 for _ in range(n)]
    i = 0

    for word in words[1:]:
        nums[i] += 1
        end = save[-1][-1]
        start = word[0]

        if word in save or end != start:
            i += 1
            if i == n:
                i = 0
            break
        i += 1
        save.append(word)
        if i == n:
            i = 0
    if save == words:
        return [0, 0]

    return [i+1, nums[i]+1]


'''다른 풀이'''
def solutions(n, words):
    save = [words[0][0]]
    for i, w in enumerate(words):
        if w not in save and save[-1][-1] == w[0][0]:
            save.append(w)
        else:
            return [i % n + 1, i // n + 1]
    return [0, 0]

for n, words in zip(ns, wordss):
    print(solutions(n, words))
