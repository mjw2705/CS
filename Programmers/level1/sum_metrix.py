arr1s = [[1,2],[2,3]], [[1], [2]]
arr2s = [[3,4],[5,6]], [[3],[4]]

for arr1, arr2 in zip(arr1s, arr2s):
    answer = []
    for ar1, ar2 in zip(arr1, arr2):
        ele = [x + y for x, y in zip(ar1, ar2)]
        answer.append(ele)

    print(answer)