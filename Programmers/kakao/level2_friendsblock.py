m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

# m = 6
# n = 6
# board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

# m = 4
# n = 5
# board = ["AAAAA", "AUUUA", "AUUAA", "AAAAA"]

# m = 7
# n = 2
# board = ["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"]

# m = 8
# n = 5
# board = ['HGNHU', 'CRSHV', 'UKHVL', 'MJHQB', 'GSHOT', 'MQMJJ', 'AGJKK', 'QULKK']

# m = 5
# n = 6
# board = ['AAAAAA','BBAATB','BBAATB','JJJTAA','JJJTAA']

answer = 0
board = list(map(list, board))

while True:
    cnt = 0
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j].upper() == board[i][j + 1].upper() == board[i + 1][j].upper() == board[i + 1][j + 1].upper():
                if board[i][j].isupper():
                    board[i][j] = board[i][j].replace(board[i][j], board[i][j].lower())
                    cnt += 1
                if board[i][j + 1].isupper():
                    board[i][j + 1] = board[i][j + 1].replace(board[i][j + 1], board[i][j + 1].lower())
                    cnt += 1
                if board[i + 1][j].isupper():
                    board[i + 1][j] = board[i + 1][j].replace(board[i + 1][j], board[i + 1][j].lower())
                    cnt += 1
                if board[i + 1][j + 1].isupper():
                    board[i + 1][j + 1] = board[i + 1][j + 1].replace(board[i + 1][j + 1], board[i + 1][j + 1].lower())
                    cnt += 1

    answer += cnt
    if cnt == 0:
        break

    # 삭제
    for i in range(n):
        for j in range(m):
            if board[j][i].islower():
                board[j][i] = ''

    # 블록 내리기
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if board[j][i] == '':
                for k in range(j-1, -1, -1):
                    if board[k][i] != '':
                        board[j][i] = board[k][i]
                        board[k][i] = ''
                        break

print(answer)
