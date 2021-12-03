phone_books = [["119", "97674223", "1195524421"], ["123","456","789"], ["12","123","1235","567","88"]]

for phone_book in phone_books:

    answer = True
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
    print(answer)

    # 다른 풀이
    answer = True
    phone_book.sort()

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            answer = False
            break
    print(answer)


def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            answer = False
            break
    return answer