import sys

# 11866번 요세푸스 문제 0
def queue_11866():
    n, k = map(int, sys.stdin.readline().split())

    num = [i+1 for i in range(n)]

    idx = 0
    queue = []
    while num:
        idx += k - 1
        if idx > len(num) - 1:
            idx %= len(num)
        queue.append(num.pop(idx))

    print('<' + str(queue)[1:-1] + '>')


# 1021번 회전하는 큐
def queue_1021():
    n, m = map(int, sys.stdin.readline().split())
    locate = list(map(int, sys.stdin.readline().split()))

    num = [i+1 for i in range(n)]
    cnt = 0

    for i in range(m):
        qu_len = len(num)
        qu_idx = num.index(locate[i])

        if qu_idx < qu_len // 2:
            while True:
                if num[0] == locate[i]:
                    del num[0]
                    break
                else:
                    num.append(num[0])
                    del num[0]
                    cnt += 1
        else:
            while True:
                if num[0] == locate[i]:
                    del num[0]
                    break
                else:
                    num.insert(0, num[-1])
                    del num[-1]
                    cnt += 1

    print(cnt)


if __name__ == '__main__':
    # queue_11866()
    queue_1021()