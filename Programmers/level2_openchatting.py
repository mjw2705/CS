record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234",
          "Enter uid1234 Prodo", "Change uid4567 Ryan"]

answer = []
logs = [reco.split(' ') for reco in record]
chatting = {log[1]:log[2] for log in logs if log[0] != 'Leave'}

for log in logs:
    if log[0] == 'Enter':
        answer.append(f'{chatting[log[1]]}님이 들어왔습니다.')
    elif log[0] == 'Leave':
        answer.append(f'{chatting[log[1]]}님이 나갔습니다.')

print(answer)