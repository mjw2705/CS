enter_list = [[1, 3, 2], [1, 4, 2, 3], [3, 2, 1], [3, 2, 1], [1, 4, 2, 3]]
leave_list = [[1, 2, 3], [2, 1, 3, 4], [2, 1, 3], [1, 3, 2], [2, 1, 4, 3]]

for enter, leave in zip(enter_list, leave_list):
    result = [0] * len(enter)
    for i in range(1, len(enter)+1):
        for j in range(i+1, len(enter)+1):
            # j가 나중에 들어오고 먼저 나감
            if enter.index(i) < enter.index(j) and leave.index(i) > leave.index(j):
                result[i - 1] += 1
                result[j - 1] += 1
            # j가 먼저 들어오고 나중에 나감
            elif enter.index(i) > enter.index(j) and leave.index(i) < leave.index(j):
                result[i - 1] += 1
                result[j - 1] += 1
            # j가 나중에 나갔고, j보다 늦게 들어온 ii가 먼저 나감
            elif leave.index(i) < leave.index(j):
                for ii in range(leave.index(i)-1, -1, -1):
                    if enter.index(leave[ii]) > enter.index(j):
                        result[i - 1] += 1
                        result[j - 1] += 1
            # j가 먼저 나가고 j보다 늦게 들어온 ii가 먼저 나가고, ii가 i보다 나중에 들어옴
            elif leave.index(i) > leave.index(j):
                for ii in range(leave.index(j)-1, -1, -1):
                    if enter.index(leave[ii]) > enter.index(j) and enter.index(leave[ii]) > enter.index(i):
                        result[i - 1] += 1
                        result[j - 1] += 1

    print(result)