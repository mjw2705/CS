import sys

N = int(sys.stdin.readline())
dic = {}
for _ in range(N):
    word = sys.stdin.readline().strip()
    dic[word] = len(word)

sort_dic = sorted(dic.items(), key=lambda x:(x[1], x[0]))
for word in sort_dic:
    print(word[0])