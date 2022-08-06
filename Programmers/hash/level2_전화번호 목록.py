phone_books = ["119", "97674223", "1195524421"], ["123","456","789"], ["12","123","1235","567","88"]


# def solution(phone_book):
#     phone_book.sort()
#     for i in range(len(phone_book)-1):
#         length = len(phone_book[i])
#         if phone_book[i] == phone_book[i+1][:length]:
#             return False
#         else:
#             return True

# def solution(phone_book):
#     for phone in phone_book:
#         length = len(phone)

#         for p in phone_book:
#             if phone != p and len(p) >= length:
#                 if p[:length] == phone:
#                     return False
#     return True

def solution(phone_book):
    dic = {}
    for phone in phone_book:
        dic[phone] = 1
    for phone in phone_book:
        tmp = ''
        for i in phone:
            tmp += i
            if tmp != phone and tmp in dic:
                return False
    return True

for phone_book in phone_books:
    print(solution(phone_book))