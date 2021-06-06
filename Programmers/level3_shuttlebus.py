ns = [1, 2, 2, 1, 1, 10]
ts = [1, 10, 1, 1, 1, 60]
ms = [5, 2, 2, 5, 1, 45]
timetables = [["08:00", "08:01", "08:02", "08:03"],
             ['09:10', '09:09', '08:00'],
             ['09:00', '09:00', '09:00', '09:00'],
             ['00:01', '00:01', '00:01', '00:01', '00:01'],
             ['23:59'],
             ['23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59']]


for n, t, m, timetable in zip(ns, ts, ms, timetables):
    answer = ''
    timetable = sorted(timetable)

    dict_bus = {}
    for i in range(n):
        bus_time = 9 * 60 + t * i
        bus_time = f'{str(bus_time // 60).zfill(2)}:{str(bus_time % 60).zfill(2)}'
        dict_bus[bus_time] = []

    bus_time = list(dict_bus.keys())
    for time in timetable:
        for bus in bus_time:
            if time <= bus and len(dict_bus[bus]) < m:
                dict_bus[bus].append(time)
                break

    target = dict_bus[bus_time[-1]]

    if len(target) < m:
        answer = bus_time[-1]
    else:
        h, m = target[-1].split(':')
        time = int(h) * 60 + int(m) - 1
        answer = f'{str(time // 60).zfill(2)}:{str(time % 60).zfill(2)}'

    print(answer)

