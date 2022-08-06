participants = ["leo", "kiki", "eden"], ["marina", "josipa", "nikola", "vinko", "filipa"], ["mislav", "stanko", "mislav", "ana"]
completions = ["eden", "kiki"], ["josipa", "filipa", "marina", "nikola"], ["stanko", "ana", "mislav"]


from collections import Counter

def solution(participant, completion):
    part = Counter(participant)
    complete = Counter(completion)

    loss = part - complete
    return list(loss)[0]


# def solution(participant, completion):
#     participant.sort()
#     completion.sort()

#     for p, c in zip(participant, completion):
#         if p != c:
#             return p
#     return participant[-1]

# from collections import defaultdict
# def solution(participant, completion):
#     dic = defaultdict(list)

#     for part in participant:
#         dic[part].append(part)
#     for comp in completion:
#         dic[comp].pop()
#         if not dic[comp]:
#             del dic[comp]
#     return list(dic.keys())[0]
    
for participant, completion in zip(participants, completions):
    print(solution(participant, completion))
