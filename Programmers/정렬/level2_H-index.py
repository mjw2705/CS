citations = [3, 0, 6, 1, 5]


def solution(citations):
    citations = sorted(citations)


    for i, citation in enumerate(citations):
        if citation >= len(citations) - i:
            return len(citations) - i
    return 0

print(solution(citations))