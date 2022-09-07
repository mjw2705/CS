import sys

# '''시간 초과'''
# N, M = map(int, sys.stdin.readline().split(' '))
# names = [sys.stdin.readline().strip() for _ in range(N)]
# names.insert(0, '0')

# for _ in range(M):
#     a = str(sys.stdin.readline().strip())
#     if a.isdigit():
#         print(names[int(a)])
#     else:
#         print(names.index(a))

'''딕셔너리 사용'''
N, M = map(int, sys.stdin.readline().split(' '))
dic_names = {}
dic_id = {}
for i in range(N):
    name = sys.stdin.readline().strip()
    dic_names[i+1] = name
    dic_id[name] = i+1

for _ in range(M):
    a = str(sys.stdin.readline().strip())
    if a.isdigit():
        print(dic_names[int(a)])
    else:
        print(dic_id[a])