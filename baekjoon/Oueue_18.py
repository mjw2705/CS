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


# if __name__ == '__main__':
#     queue_11866()
