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
#     answer = []
#     gem_set = set(gems)
#     start, end = 0, 0
#     bucket = {}
#
#     while end < len(gems):
#         if gems[end] not in bucket:
#             bucket[gems[end]] = 1
#         else:
#             bucket[gems[end]] += 1
#         end += 1
#
#         if set(bucket) == gem_set:
#             while start < end:
#                 if gems[start] in bucket and bucket[gems[start]] > 1:
#                     bucket[gems[start]] -= 1
#                     start += 1
#                 else:
#                     break
#     answer = [start + 1, end]
#     print(answer)


'''정답'''
for gems in gemss:
    answer = []
    gem_set = set(gems)
    start, end = 0, 0
    bucket =  {}
    shortest = len(gems) + 1

    while end < len(gems):
        if gems[end] not in bucket:
            bucket[gems[end]] = 1
        else:
            bucket[gems[end]] += 1
        end += 1

        if len(gem_set) == len(bucket):
            while start < end:
                if gems[start] in bucket and bucket[gems[start]] > 1:
                    bucket[gems[start]] -= 1
                    start += 1
                elif shortest > end - start:
                    shortest = end - start
                    answer = [start+1, end]
                    break
                else:
                    break
    print(answer)
