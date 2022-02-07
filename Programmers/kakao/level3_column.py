ns = [5, 5]
build_frames = [[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]],
[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]]


def check(answer):
    for x, y, what in answer:
        # 기둥
        if what == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False
        # 보
        else:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True

for n, build_frame in zip(ns, build_frames):
    ans = []
    for build_f in build_frame:
        x, y, what, how = build_f

        if how == 1:
            ans.append([x, y, what])
            if not check(ans):
                ans.remove([x, y, what])
        else:
            ans.remove([x, y, what])
            if not check(ans):
                ans.append([x, y, what])

    answer = sorted(ans, key=lambda  x :(x[0], x[1], x[2]))
    print(answer)