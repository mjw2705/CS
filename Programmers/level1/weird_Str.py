s = "try hello world"

answer = ''
words = s.split(' ')
for word in range(len(words)):
    for i in range(len(words[word])):
        if i % 2 == 0:
            answer += words[word][i].upper()
        else:
            answer += words[word][i].lower()

    if word != len(words) - 1:
        answer += ' '

print(answer)