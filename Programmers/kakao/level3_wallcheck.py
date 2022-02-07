n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]


from itertools import permutations

def solution(n, weak, dist):
    weak_len = len(weak)
    for i in range(weak_len):
        weak.append(weak[i] + n)
    # [1, 5, 6, 10, 13, 17, 18, 22] 시계/반시계

    answer = len(dist) + 1 # 투입할 수 있는 최대 친구 수 + 1 불가능한 경우

    for i in range(weak_len):
        # 어디서부터 점검 시작
        start = [weak[j] for j in range(i, i+weak_len)]
        candidate = permutations(dist, len(dist)) # 투입할 친구 순서

        for order in candidate:
            friend_idx, friend_cnt = 0, 1

            check_len = start[0] + order[friend_idx]

            for idx in range(weak_len):
                if start[idx] > check_len:
                    friend_cnt += 1

                    if friend_cnt > len(order):
                        break

                    friend_idx += 1
                    check_len = order[friend_idx] + start[idx]

            answer = min(answer, friend_cnt)

    if answer > len(dist):
        return -1

    return answer

print(solution(n, weak, dist))
