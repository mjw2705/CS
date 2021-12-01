from collections import Counter

participants = [["leo", "kiki", "eden"], ["marina", "josipa", "nikola", "vinko", "filipa"], ["mislav", "stanko", "mislav", "ana"]]
completions = [["eden", "kiki"], ["josipa", "filipa", "marina", "nikola"], ["stanko", "ana", "mislav"]]


for participant, completion in zip(participants, completions):
    # 효율성 0
    '''
    answer = ''
    for comple in completion:
        if comple in participant:
            participant.remove(comple)
    answer += participant[0]
    '''

    part = Counter(participant)
    com = Counter(completion)
    ans = part - com
    answer = list(ans.keys())[0]
    print(answer)



from collections import Counter

def solution(participant, completion):
    ans = Counter(participant) - Counter(completion)
    answer = list(ans.keys())[0]
    return answer

