# 11047번
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


# 1931번
num = int(input())
time = [list(map(int, input().split())) for _ in range(num)]
sort_time = sorted(time, key=lambda x: x[0])

print(sort_time)
# if __name__ == '__main__':
    # greedy_11047()