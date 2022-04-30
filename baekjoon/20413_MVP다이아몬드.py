# N = 3
# s, g, p, d = 30, 60, 90, 150
# grade = 'BSG'
N = 10
s, g, p, d = 257, 269, 367, 500
grade = 'BSGGGGPPDD'

# N = int(input())
# s, g, p, d = list(map(int, input().split()))
# grade = str(input())

money = [0]
mvp_grade = ['S', 'G', 'P', 'D']
stand = [s, g, p, d]

for grad in grade:
    if grad == 'B':
        price = stand[0] - 1
        m = price - money[-1]
        money.append(m)
    elif grad == 'D':
        price = stand[-1]
        money.append(price)
    else:
        idx = mvp_grade.index(grad)
        price = stand[idx + 1] - 1
        m = price - money[-1]
        money.append(m)

max_money = sum(money)
print(max_money)