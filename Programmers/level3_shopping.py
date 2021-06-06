from collections import Counter

gemss = [["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
        ["AA", "AB", "AC", "AA", "AC"],
        ["XYZ", "XYZ", "XYZ"],
        ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]]

'''
정확성: 15.6
효율성: 4.4
합계: 20.0 / 100.0'''
# for gems in gemss:
#     gem_set = set(gems)
#     start, end = 0, 0
#     bucket = {}
#
#     while end < len(gems):
#         if gems[end] not in bucket:
#             bucket[gems[end]] = 1
#         else:
#             bucket[gems[end]] += 1
#         if set(bucket) == gem_set:
#             break
#         else:
#             end += 1
#
#     while start < len(gems):
#         if gems[start] in bucket and bucket[gems[start]] != 1:
#             bucket[gems[start]] -= 1
#             start += 1
#         else:
#             break
#     answer = [start+1, end+1]
#     print(answer)


'''
정확성: 15.6
효율성: 4.4
합계: 20.0 / 100.0'''
for gems in gemss:
    answer = []
    gem_set = set(gems)
    start, end = 0, 0
    bucket = {}

    while end < len(gems):
        if gems[end] not in bucket:
            bucket[gems[end]] = 1
        else:
            bucket[gems[end]] += 1
        end += 1

        if set(bucket) == gem_set:
            while start < end:
                if gems[start] in bucket and bucket[gems[start]] > 1:
                    bucket[gems[start]] -= 1
                    start += 1
                else:
                    break
    answer = [start + 1, end]
    print(answer)