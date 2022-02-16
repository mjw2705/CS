ss = "a234", "1234"

def solution(s):
    # if len(s) == 4 or len(s) == 6:
    if len(s) in (4, 6):
        return s.isdigit()
    return False

for s in ss:
    print(solution(s))