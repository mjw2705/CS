# 11047번 동전0
def greedy_11047():
    num, value = map(int, input().split())
    v_list = [int(input()) for _ in range(num)]

    min_value = 0
    for i in reversed(v_list):
        if value == 0:
            break
        if i > value:
            continue
        else:
            min_value += value // i
            value = value % i

    print(min_value)


# 1931번 회의실 배정
def greedy_1931():
    num = int(input())
    meet_time = [list(map(int, input().split())) for _ in range(num)]
    sort_meet = sorted(meet_time, key=lambda x: (x[1], x[0]))

    # meet = [0 for _ in range(num)]
    #
    # for i in range(num):
    #     cnt = 1
    #     end = sort_meet[i][1]
    #     for ti in sort_meet[i+1:]:
    #         if end <= ti[0]:
    #             cnt += 1
    #             end = ti[1]
    #     meet[i] = cnt
    #
    # print(max(meet))

    end = 0
    max_meet = 0
    print(sort_meet)
    for ti in sort_meet:
        if ti[0] >= end:
            end = ti[1]
            max_meet += 1

    print(max_meet)


# 11399번 ATM
def greedy_11399():
    num = int(input())
    time = list(map(int, input().split()))

    sort_time = sorted(time)

    cnt = 0
    for i in range(num):
        cnt += sum(sort_time[i::-1])
    print(cnt)


if __name__ == '__main__':
    # greedy_11047()
    greedy_1931()
    # greedy_11399()