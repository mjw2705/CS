play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00",
        "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

# play_time = "50:00:00"
# adv_time = "50:00:00"
# logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]


def solution(play_time, adv_time, logs):
    def time_to_int(time):
        h, m, s = time.split(':')
        return 3600 * int(h) + 60 * int(m) + int(s)

    def int_to_time(time):
        h = str(time // 3600).zfill(2)
        m = str((time % 3600) // 60).zfill(2)
        s = str((time % 3600) % 60).zfill(2)
        return f'{h}:{m}:{s}'


    play = time_to_int(play_time)
    adv = time_to_int(adv_time)

    times = [0 for i in range(play + 1)]

    for log in logs:
        start, end = log.split('-')
        start = time_to_int(start)
        end = time_to_int(end)
        times[start] += 1
        times[end] -= 1

    # 초당 시청자 수
    for i in range(len(times)):
        times[i] += times[i-1]

    # 누적 시청자 수
    for i in range(len(times)):
        times[i] += times[i-1]

    most_view = 0
    max_time = 0
    for i in range(adv, play):
        if most_view < times[i] - times[i-adv]:
            most_view = times[i] - times[i - adv]
            max_time = i - adv + 1

    return int_to_time(max_time)


print(solution(play_time, adv_time, logs))
