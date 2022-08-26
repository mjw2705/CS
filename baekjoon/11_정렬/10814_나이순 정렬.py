import sys

N = int(sys.stdin.readline())
mems = []
for _ in range(N):
    age, name = map(str, sys.stdin.readline().split())
    mems.append([int(age), name])

mems.sort(key=lambda x:x[0])
for mem in mems:
    print(int(mem[0]), mem[1])

# dic = {}
# for i in range(N):
#     age, name = map(str, sys.stdin.readline().split())
#     dic[i] = [int(age), name]
# sort_arr = sorted(dic.items(), key=lambda x: (x[1][0], x[0]))
# for arr in sort_arr:
#     print(arr[1][0], arr[1][1])