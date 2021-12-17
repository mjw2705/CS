prices = [1, 2, 3, 2, 3]


answer = [0] * len(prices)
for i in range(len(prices)):
    for j in range(i+1, len(prices)):
        if prices[i] > prices[j]:
            answer[i] += 1
            break
        else:
            answer[i] += 1

print(answer)


'''stack 사용'''
answer = [0] * len(prices)
stack = []

for i in range(len(prices)):
    while stack and prices[i] < prices[stack[-1]]:
        j = stack.pop()
        answer[j] = i - j
    stack.append(i)

while stack:
    j = stack.pop()
    answer[j] = len(prices) - 1 - j

print(answer)