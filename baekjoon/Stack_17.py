# 1874번 스택 수열
import sys

n = int(sys.stdin.readline())
output_list = [int(sys.stdin.readline()) for _ in range(n)]

output = []
num = []
cnt = 1
for i in range(n):
    while cnt <= output_list[i]:
        num.append(cnt)
        output.append('+')
        cnt += 1
    if num[-1] == output_list[i]:
        output.append('-')
        num.pop(-1)

# 리스트가 비어있지 않으면 NO
if num:
    print('NO')
else:
    for i in output:
        print(i)
