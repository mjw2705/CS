answerss = [[1, 2, 3, 4, 5], [1, 3, 2, 4, 2]]

for answers in answerss:

    answer = []
    first = [1, 2, 3, 4, 5] * 2000
    second = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    q_len = len(answers)
    first_q = first[:q_len]
    second_q = second[:q_len]
    third_q = third[:q_len]

    first_ans = [i for i, j in zip(first_q, answers) if i == j]
    second_ans = [i for i, j in zip(second_q, answers) if i == j]
    third_ans = [i for i, j in zip(third_q, answers) if i == j]

    ans_max = max([len(first_ans), len(second_ans), len(third_ans)])

    if ans_max == len(first_ans):
        answer.append(1)
    if ans_max == len(second_ans):
        answer.append(2)
    if ans_max == len(third_ans):
        answer.append(3)

    print(answer)


    '''다른 사람 풀이'''
    result = []
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]

    for i, answer in enumerate(answers):
        if answer == pattern1[i % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[i % len(pattern2)]:
            score[1] += 1
        if answer == pattern3[i % len(pattern3)]:
            score[2] += 1

    for idx, sco in enumerate(score):
        if sco == max(score):
           result.append(idx+1)

    print(result)


def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5] * 2000
    second = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    q_len = len(answers)
    first_q = first[:q_len]
    second_q = second[:q_len]
    third_q = third[:q_len]

    first_ans = [i for i, j in zip(first_q, answers) if i == j]
    second_ans = [i for i, j in zip(second_q, answers) if i == j]
    third_ans = [i for i, j in zip(third_q, answers) if i == j]

    ans_max = max([len(first_ans), len(second_ans), len(third_ans)])

    if ans_max == len(first_ans):
        answer.append(1)
    if ans_max == len(second_ans):
        answer.append(2)
    if ans_max == len(third_ans):
        answer.append(3)

    return answer