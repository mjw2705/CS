browns = 10, 8, 24
yellows = 2, 1, 24

for brown, yellow in zip(browns, yellows):

    total = brown + yellow

    for h in range(1, total + 1):
        if (total / h) % 1 == 0:
            w = int(total / h)

            if w >= h:
                if (w - 2) * (h - 2) == yellow and 2 * (w + h) - 4 == brown:
                    print([w, h])


def solution(brown, yellow):
    total = brown + yellow

    for h in range(1, total + 1):
        if (total / h) % 1 == 0:
            w = int(total / h)

            if w >= h:
                if (w - 2) * (h - 2) == yellow and 2 * (w + h) - 4 == brown:
                    return ([w, h])