user_ids = [["frodo", "fradi", "crodo", "abc123", "frodoc"],
            ["frodo", "fradi", "crodo", "abc123", "frodoc"],
            ["frodo", "fradi", "crodo", "abc123", "frodoc"]]
banned_ids = [["fr*d*", "abc1**"],
              ["*rodo", "*rodo", "******"],
              ["fr*d*", "*rodo", "******", "******"]]


for user_id, banned_id in zip(user_ids, banned_ids):
    bans = [[]]
    for banned in banned_id:
        ban = []
        users = []
        length = len(banned)
        for user in user_id:
            if length == len(user):
                users.append(user)
        user_copy = users.copy()
        while '*' in banned:
            idx = banned.find('*')
            banned = banned[:idx] + banned[idx + 1:]
            for i in range(len(user_copy)):
                user_copy[i] = user_copy[i][:idx] + user_copy[i][idx+1:]

        for b in bans:
            for i in range(len(user_copy)):
                if banned == user_copy[i]:
                    if users[i] not in b:
                        ban.append(b + [users[i]])
            bans = ban
    answer = []
    for b in bans:
        if set(b) not in answer:
            answer.append(set(b))
    print(len(answer))


# for user_id, banned_id in zip(user_ids, banned_ids):
#
#     bans = [[]]
#     for banned in banned_id:
#         ban = []
#         for user in user_id:
#             if len(user) != len(banned):
#                 continue
#             chk = True
#             for i in range(len(user)):
#                 if banned[i] != '*' and user[i] != banned[i]:
#                     chk = False
#                     break
#             if chk:
#                 for b in bans:
#                     if user not in b:
#                         ban.append(b+[user])
#                         # print(ban)
#         bans = ban
#         # print(bans)
#     answer = []
#     for b in bans:
#         if set(b) not in answer:
#             answer.append(set(b))
#
#     print(len(answer))
