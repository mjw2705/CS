# 10171
# print("\     /\\\n )   ( ')\n(   /  )\n \(__)|")


# 10172
# print("|\\_/|\n|p q|   /}\n( 0 )\"\"\"\\\n|\"^\"\'   |\n||_/=\\\\__|\n")


# 10817
# A, B, C = map(int, input().split())
# if A >= B:
#     if A >= C:
#         if B >= C:
#             print(B)
#         else:
#             print(C)
#     else:
#         print(A)
# else:
#     if B >= C:
#         if A >= C:
#             print(A)
#         else:
#             print(C)
#     else:
#         print(B)

# A = list(map(int, input().split()))
# A.sort()
# print(A[int(len(A)/2)])


# 15552
# import sys
# num = int(input())
# for i in range(num) :
#     a, b = list(map(int, sys.stdin.readline().split()))
#     print(a+b)


# N, x = map(int, input().split())
# a = list(map(int, input().split()))
# for i in range(len(a)) :
#     if a[i] < x :
#         print(a[i], end=' ')


# 10951
# import sys
# for line in sys.stdin :
#     a, b = map(int, line.split())
#     print(a+b)


# 1110
# n = input()
# if int(n) < 10:
#     n = '0' + n
#
# cnt = 0
# t = n
#
# while True:
#     cnt += 1
#     sum = int(t[0]) + int(t[1])
#
#     if sum < 10:
#         new = t[1] + str(sum)
#     else:
#         new = t[1] + str(sum)[1]
#
#     if new == n:
#         break
#     else:
#         t = new
# print(cnt)


# n = int(input())
# arr = list(map(int, input().split()))
# print("%d %d" %(min(arr),max(arr)))


# max = 0
# index = 0
# for i in range(1, 10):
#     a = int(input())
#     if a > max :
#         max = a
#         index = i
# print("%d\n%d" %(max, index))


# 2577
# a = int(input())
# b = int(input())
# c = int(input())
# result = str(a*b*c)
# for num in range(10) :
#     count = result.count(str(num))
#     print(count)


# 3052
# rest = []
# for i in range(10) :
#     a = int(input())
#     rest.append(a%42)
# result = set(rest)
# print(len(result))


# 8958
# n = int(input())
# for i in range(n) :
#     ox = list(map(str, input()))
#     sum = 0
#     c = 1
#     for k in range(len(ox)) :
#         if ox[k] == 'O' :
#             sum += c
#             c += 1
#         else :
#             c = 1
#     print(sum)


# 4344
# c = int(input())
# for i in range(c):
#     arr = list(map(int, input().split()))
#     aver = sum(arr[1:]) / arr[0]
#     num = 0
#     for k in arr[1:]:
#         if k > aver:
#             num += 1
#     print("{:0.3f}%".format((num / arr[0]) * 100))


# 4637
# def d(n) :
#     a = 0
#     for i in str(n) :
#         a += int(i)
#     return a + int(n)
# a = []
# for i in range(1,10001) :
#     b = d(i)
#     a.append(b)
# for j in range(1, 10001) :
#     if j not in a :
#         print(j)


# 1065
# num = int(input())
# hansu = 0
# for i in range(1, num+1):
#     if i <= 99 :
#         hansu += 1
#     else :
#         L_num = list(map(int, str(i)))
#         if L_num[0] - L_num[1] == L_num[1] - L_num[2] :
#             hansu += 1
# print(hansu)


# 2675
# t = int(input())
# for i in range(t):
#     a = []
#     test = input().split()
#     r = int(test[0])
#     for j in test[1] :
#         print(j*r, end='')
#     print('')


# 1157
# word = input().upper()
# word_l = list(set(word))
# count = []
# for i in word_l:
#     count.append(word.count(i))
# if count.count(max(count)) >= 2 :
#     print("?")
# else :
#     a = count.index(max(count))
#     print(word_l[a])


# 2908
# num = list(input().split())
# l1 = list(num[0])
# l2 = list(num[1])
# l1.reverse()
# l2.reverse()
# a = ''.join(l1)
# b = ''.join(l2)
# print(max(a, b))


# 5622
# word = input()
# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# time = 0
# for i in range(len(word)) :
#     for k in dial :
#         if word[i] in k :
#             time += dial.index(k) + 3
# print(time)


# 2941
# word = input()
# cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# for cr in cro :
#     word = word.replace(cr, 'a')
# print(len(word))


# 1316
# n = int(input())
# for i in range(n) :
#     word = input()
#     for j in range(1, len(word)) :
#         if word.find(word[j-1]) > word.find(word[j]) :
#             n -= 1
# print(n)

# n = int(input())
# group = 0
# for i in range(n) :
#     word = input()
#     if list(word) == sorted(word, key= word.find) :
#         group += 1
# print(group)


# 1712
# a, b, c = map(int, input().split())
# if b >= c :
#     print(-1)
# else :
#     print((a // (c - b)) + 1 )


# 2839
# n = int(input())
# box = n // 5
# n -= box * 5
#
# while box > 0:
#     if n % 3 == 0:
#         box += n // 3
#         break
#     else:
#         box -= 1
#         n += 5
#
# if box == 0:
#     print(n // 3 if n % 3 == 0 else -1)
# else:
#     print(box)


# 2292
# n = int(input())
# std_r = 1
# i = 1
# while n > std_r :
#     std_r += 6 * i
#     i += 1
# print(i)


# 1193
# i_n = int(input())
# sum_value = 1
# n = 1

# while i_n > sum_value:
#     n += 1
#     sum_value += n
#
# m_value = sum_value - i_n
# if n % 2 == 0:
#     print('{}/{}'.format(n - m_value, 1 + m_value))
# else:
#     print('{}/{}'.format(1 + m_value, n - m_value))

# x = int(input())
# cnt = 1
# sum_val = 1
#
# while x > sum_val :
#     cnt += 1
#     sum_val += cnt
#
# minus = sum_val - x
# if cnt % 2 == 0:
#     print('{}/{}'.format(cnt-minus, 1+minus))
# else:
#     print('{}/{}'.format(1+minus, cnt-minus))


# 2869
# a, b, v = map(int, input().split())
# day = 0
# d_h = 0
# while v > d_h :
#     d_h += a
#     day += 1
#     if d_h == v:
#         break
#     else:
#         d_h -= b
# print(day)

# import math
# a, b, v = map(int, input().split())
# rest = v-a
# d_h = a-b
# print(math.ceil(rest / d_h + 1))


# 10250
# t = int(input())
# for i in range(t) :
#     h, w, n = map(int, input().split())
#     room = n // h
#     floor = n - h * room
#     if (n % h) != 0:
#         room += 1
#     else: pass
#     if floor == 0:
#         floor = h
#     else: pass
#     if room < 10:
#         print(str(floor) + '0' + str(room))
#     else:
#         print(str(floor) + str(room))


# 2775
# for _ in range(int(input())):
#     k = int(input())
#     n = int(input())
#
#     arr = [[0 for _ in range(15)] for _ in range(15)]
#
#     for i in range(15):
#         for j in range(1, 15):
#             if i == 0:
#                 arr[i][j] = j
#             elif j == 1:
#                 arr[i][j] = 1
#             else:
#                 arr[i][j] = arr[i][j - 1] + arr[i - 1][j]
#
#     print(arr[k][n])


# 1011
# t = int(input())
# for i in range(t):
#     x, y = map(int, input().split())
# num = 1
# dis = 0
# while x <= y-1 :


# 5543
# a = 2000
# c = 2000
# for _ in range(3) :
#     b = int(input())
#     a = min(a,b)
# for _ in range(2) :
#     d = int(input())
#     c = min(c, d)
# print(a + c - 50)


# 1978
# n = int(input())
# num = list(map(int, input().split()))
#
# cnt = 0
# for i in num:
#     if i == 1:
#         continue
#     check = True
#     for j in range(2, i):
#         if i % j == 0:
#             check = False
#             break
#     if check:
#         cnt += 1
# print(cnt)


# 10872
# def factorial(n) :
#     if n == 1:
#         return 1
#     else :
#         return n*factorial(n-1)
# print(factorial(int(input())))

# from math import factorial
# print(factorial(int(input())))


# 10870
# def peb(n):
#     if n == 0:
#         return 0
#     elif n ==1 :
#         return 1
#     else :
#         return peb(n-1) + peb(n-2)
# print(peb(int(input())))
