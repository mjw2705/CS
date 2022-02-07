places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]


def solution(places):
    answer = []

    for place in places:
        flag = False

        for x in range(5):
            if flag:
                break
            for y in range(5):
                if flag:
                    break

                if place[x][y] == 'P':

                    if y+1 < 5:
                        if place[x][y+1] == 'P':
                            flag = True
                            break
                        if place[x][y+1] == 'O':
                            if place[x][y+2] == 'P':
                                flag = True
                                break
                    if x+1 < 5:
                        if place[x+1][y] == 'P':
                            flag = True
                            break
                        if place[x+1][y] == 'O':
                            if place[x+2][y] == 'P':
                                flag = True
                                break

                    if x+1 < 5 and y+1 < 5:
                        if place[x+1][y+1] == 'P' and (place[x][y+1] == 'O' or place[x+1][y] == 'O'):
                            flag = True
                            break

                    if x+1 < 5 and y-1 >= 0:
                        if place[x+1][y-1] == 'P' and (place[x][y-1] == 'O' or place[x+1][y] == 'O'):
                            flag = True
                            break

        if flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer

print(solution(places))

