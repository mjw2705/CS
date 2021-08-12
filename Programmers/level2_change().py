ps = "(()())()", ")(", "()))((()"

def is_balance(w):
    check = 0
    for w_ in w:
        if w_ == '(':
            check += 1
        else:
            check -= 1
    return not bool(check)

def is_correct(w):
    stack = []
    for w_ in w:
        if w_ == '(':
            stack.append(w_)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    return True

def solution(p):
    if is_correct(p) == True:
        return p

    for i in range(2, len(p)+1, 2):
        if is_balance(p[:i]) == True:
            u, v = p[:i], p[i:]
            break

    if is_correct(u) == True:
        return u + solution(v)
    else:
        result = '(' + solution(v) + ')'
        for u_ in u[1:-1]:
            if u_ == '(':
                result += ')'
            else:
                result += '('

    return result

for p in ps:
    print(solution(p))