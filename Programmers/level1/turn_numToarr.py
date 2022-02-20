n = 12345

answer = []
n = str(n)
for i in range(len(n)-1, -1, -1):
    answer.append(int(n[i]))
print(answer)

print(list(map(int, reversed(n))))