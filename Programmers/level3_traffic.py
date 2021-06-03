# lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
# lines = ["2016-09-15 20:59:57.421 0.351s",
#          "2016-09-15 20:59:58.233 1.181s",
#          "2016-09-15 20:59:58.299 0.8s",
#          "2016-09-15 20:59:58.688 1.041s",
#          "2016-09-15 20:59:59.591 1.412s",
#          "2016-09-15 21:00:00.464 1.466s",
#          "2016-09-15 21:00:00.741 1.581s",
#          "2016-09-15 21:00:00.748 2.31s",
#          "2016-09-15 21:00:00.966 0.381s",
#          "2016-09-15 21:00:02.066 2.62s"]


def solution(lines):
    def cnttime(start, times):
        cnt = 0
        end = start + 1000 - 1
        for time in times:
            if start <= time[1] and end >= time[0]:
                cnt += 1
        return cnt

    times = []
    for line in lines:
        date, finish_t, T = line.split(' ')
        t = float(T[:-1]) * 1000
        hh, mm, ss = finish_t.split(':')
        end = (int(hh) * 3600 + int(mm) * 60 + float(ss)) * 1000
        start = end - t + 1
        times.append([start, end])

    answer = 0
    for time in times:
        answer = max(answer, cnttime(time[0], times), cnttime(time[1], times))

    return answer


print(solution(lines))

