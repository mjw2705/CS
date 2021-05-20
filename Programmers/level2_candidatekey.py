relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

from itertools import combinations


def solution(relation):
    answer = 0
    n_row = len(relation) # 6
    n_col = len(relation[0]) # 4

    candidate = []
    for i in range(1, n_col+1):
        candidate.extend(combinations(range(n_col), i))

    unique = []
    for candi in candidate:
        candis = [tuple([rela[i] for i in candi]) for rela in relation]
        if len(set(candis)) == n_row:
            unique.append(candi)
    # [(0,), (0, 1), (0, 2), (0, 3), (1, 2), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]

    answer = set(unique)
    # {(0, 1), (1, 2), (0,), (0, 1, 2), (0, 2, 3), (0, 1, 3), (1, 2, 3), (0, 3), (0, 2), (0, 1, 2, 3)}
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])

    return len(answer)