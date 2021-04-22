board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
result = 4


basket = []
count = 0
for i in moves:
    for j in range(len(board)):
        if board[j][i-1] == 0:
            pass
        else:
            basket.append(board[j][i-1])
            board[j][i-1] = 0
            break

    if len(basket) > 1:
        if basket[-1] == basket[-2]:
            count += 2
            del basket[-1]
            del basket[-1]

answer = count
print(answer)

