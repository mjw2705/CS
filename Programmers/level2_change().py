import re

# 올바른 문자열인지 확인
def correct_str(p):
    stack = []
    check = False
    for i in p:
        if len(stack) == 0:
            if i == "(":
                stack += i
                check = True
            else:
                check = False
                break
        elif i == "(":
            stack += i
        elif i == ")":
            stack.pop()
    return stack, check


# p = ")("
p = "()))((()"

answer = ""
stack, check = correct_str(p)
correct = ""
balance = ""
u = ""
v = ""
if not stack and check:
    answer = p
elif not check:
    # 2
    for i in range(len(p)//2):
        u = p[i*2:i*2+2]
        idx = i*2+2
        if u.count("(") == u.count(")"):
            break
    v = p[idx:]
    # 3
    stack, check = correct_str(u)
    if not stack and check:
        answer += u
    # else:


print(u)
print(v)

#     stack += i
#     print(stack)
#     if len(stack) > 1:
#         if stack[-2] == "(" and stack[-1] == ")":
#             stack = stack.replace(stack[-1], "")
#             stack = stack.replace(stack[-1], "")
#     print(stack)
# print(stack)


