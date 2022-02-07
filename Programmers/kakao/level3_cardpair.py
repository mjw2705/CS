# board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
# r = 1
# c = 0
board = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
r = 0
c = 1

from collections import defaultdict
from itertools import permutations


'''정확도 60%'''
def solution(board, r, c):
    def get_move(r, c, dx, dy):
        if dx != r and dy != c:
            return 2
        elif dx == r and dy == c:
            return 0
        else:
            return 1

    answer = []
    card_index = defaultdict(list)

    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card_index[board[i][j]].append((i, j))


    card_num = [i for i in range(1, len(card_index) + 1)]

    for orders in permutations(card_num, len(card_num)):

        move_cnt = 0
        p_r , p_c = r, c

        for num in orders:
            points = []
            for card_x, card_y in card_index[num]:
                points.append((get_move(p_r, p_c, card_x, card_y), card_x, card_y))

            # 카드 1이 카드 2보다 가까우면
            if points[0][0] < points[1][0]:
                move_cnt += points[0][0]
                p_r, p_c = points[0][1], points[0][2] # 현재 위치를 카드 1의 위치로
                dx, dy = points[1][1], points[1][2]
                move_cnt += get_move(p_r, p_c, dx, dy) # 카드 2까지 다시 이동
                p_r, p_c = dx, dy

            else:
                move_cnt += points[1][0]
                p_r, p_c = points[1][1], points[1][2]  # 현재 위치를 카드 2의 위치로
                dx, dy = points[0][1], points[0][2]
                move_cnt += get_move(p_r, p_c, dx, dy)  # 카드 1까지 다시 이동
                p_r, p_c = dx, dy

        answer.append(move_cnt + len(card_index) * 2) # 엔터는 카드수 * 2개

    return min(answer)

print(solution(board, r, c))