# n = 5
# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]

n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]


answer = []
map1 = []
map2 = []

for ar1, ar2 in zip(arr1, arr2):
    num1 = bin(ar1)[2:]
    num1 = num1.zfill(n)
    map1.append(num1)

    num2 = bin(ar2)[2:]
    num2 = num2.zfill(n)
    map2.append(num2)

ans = ''
for ar1, ar2 in zip(map1, map2):
    for a1, a2 in zip(ar1, ar2):
        num = int(a1) | int(a2)
        if num == 0:
            ans = ' '
        else:
            ans = '#'
        answer.append(ans)

answer = ''.join(answer)
answer = [answer[i * n:(i+1) * n] for i in range(len(answer) // n)]
print(answer)


# 다른 사람 풀이
answer = []
for ar1, ar2 in zip(arr1, arr2):
    ans = bin(ar1 | ar2)[2:]
    ans = ans.rjust(n, '0')
    ans = ans.replace('1', '#')
    ans = ans.replace('0', ' ')
    answer.append(ans)

print(answer)