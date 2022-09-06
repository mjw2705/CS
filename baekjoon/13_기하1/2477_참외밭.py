import sys

# K = int(sys.stdin.readline())
# direct = []
# length = []
# for _ in range(6):
#     d, l = map(int, sys.stdin.readline().split(' '))
#     direct.append(d)
#     length.append(l)

# total = 1
# for i in range(1, 5):
#     if direct.count(i) == 2:
#         idxs = list(filter(lambda x: direct[x] == i, range(len(direct))))
#         a = 0
#         for idx in idxs:
#             a += length[idx]
#         total *= a

# compare=[1, 3], [4, 1], [2, 4], [3, 2]

# for c in compare:
#     for i in range(4):
#         if direct[i:i+2] == c:
#             s = length[i] * length[i+1]

# print((total - s) * K)


K = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(6)]
compare=[1, 3], [4, 1], [2, 4], [3, 2]

max_w = 0
max_h = 0
w_i, h_i = 0, 0
for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if max_w < arr[i][0]:
            max_w = arr[i][1]
            w_i = i
    elif arr[i][0] == 3 or arr[i][0] == 4:
        if max_h < arr[i][0]:
            max_h = arr[i][1]
            h_i = i

sub_w = abs(arr[(w_i - 1) % 6][1] - arr[(w_i + 1) % 6][1])
sub_h = abs(arr[(h_i - 1) % 6][1] - arr[(h_i + 1) % 6][1])

print((max_w * max_h - sub_w * sub_h) * K)
