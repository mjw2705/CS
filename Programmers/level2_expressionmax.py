import itertools
import re

expressions = ["50*6-3*2", "100-200*300-500+20"]

for expression in expressions:
    answer = 0

    operator = []
    for exp in expression:
        if not exp.isdigit() and exp not in operator:
            operator.append(exp)  # ['*', '-']

    noperator = list(itertools.permutations(operator, len(operator)))
    nums = re.split('(\D)', expression)  # ['50', '*', '6', '-', '3', '*', '2']

    answers = []
    for oper in noperator:
        num = nums.copy()

        for op in oper:
            while op in num:
                idx = num.index(op)
                num[idx-1] = str(eval(num[idx-1] + num[idx] + num[idx+1]))
                num = num[:idx] + num[idx+2:]  # ['300', '-', '3', '*', '2']

        answers.append(abs(int(num[0])))

    answer = max(answers)
    print(answer)
