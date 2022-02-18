ss = "AB", "z", "a B z"
ns = 1, 1, 4

import string

def solution(s):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    answer = ''
    for i in s:
        if i.isalpha():
            if i.islower():
                idx = lower.find(i)
                to_idx = idx + n
                if to_idx >= len(lower):
                    to_idx -= len(lower)
                answer += lower[to_idx]
            else:
                idx = upper.find(i)
                to_idx = idx + n
                if to_idx >= len(upper):
                    to_idx -= len(upper)
                answer += upper[to_idx]  
        else:
            answer += i
    return answer