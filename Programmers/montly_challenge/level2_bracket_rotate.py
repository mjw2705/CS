ss = "[](){}", "}]()[{", "[)(]", "}}}"

for s in ss:

    answer = 0
    for x in range(len(s)):

        bracket = s[x:] + s[:x]
        stack = [bracket[0]]

        for brac in bracket[1:]:
            stack.append(brac)

            if len(stack) >= 2:
                if stack[-2] == '(':
                    if stack[-1] == ')':
                        del stack[-2:]

                elif stack[-2] == '{':
                    if stack[-1] == '}':
                        del stack[-2:]

                elif stack[-2] == '[':
                    if stack[-1] == ']':
                        del stack[-2:]
        if not stack:
            answer += 1

    print(answer)
