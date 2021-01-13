"""
버블 정렬

연속된 두 개의 index를 비교해서 앞의 숫자가 뒤의 숫자보다 크면 자리 교체, 큰 숫자가 차례차례 뒤로 가는 구조
한번 순회가 끝나면 처음부터 비교, 한번 루틴을 돌 때마다 큰 숫자가 뒤에 위치하기 때문에 비교할 횟수가 줄어듦
비교 횟수 = n(n-1)/2
시간복잡도 = O(n^2)
"""
def Bubble_sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j+1]:
                # a[j], a[j+1] = a[j+1], a[j]
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return a


'''
선택 정렬

배열을 순회하면서 현재 값보다 작은 값을 찾아 가장 작은 값과 자리 교체, 작은 숫자가 차례차례 앞으로 가는 구조
비교 횟수 = n(n-1)/2
시간복잡도 = O(n^2)
'''
def Selection_sort(a):
    for i in range(len(a) - 1):
        minidx = i
        for j in range(i+1, len(a)):
            if a[minidx] > a[j]:
                minidx = j
        # a[i], a[minidx] = a[minidx], a[i]
        temp = a[i]
        a[i] = a[minidx]
        a[minidx] = temp

    return a


'''
삽입 정렬

두번째 인덱스부터 시작하여 그 앞의 인덱스들과 비교해서 삽입될 위치를 정한다.
앞의 인덱스보다 작으면 앞 인덱스를 한 칸씩 뒤로 이동시키고 해당 위치에 삽입
비교 횟수 = 최선:n-1, 최악:n(n-1)/2
시간 복잡도 = O(n), O(n^2)
'''
def Insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        for j in reversed(range(i)):
            if a[j] > key:
                # a[j+1], a[j] = a[j], key
                a[j+1] = a[j]
                a[j] = key
    return a


'''
퀵 정렬

첫번째 인덱스를 피벗으로 선택하여 피벗보다 작은 요소들은 피벗의 왼쪽, 피벗보다 큰 요소들은 피벗의 오른쪽으로 붙인다. 
피벗의 왼쪽, 오른쪽 리스트들을 다시 똑같이 피벗을 정해 정렬(재귀)
시간 복잡도 = O(nlogn)
'''
def Quick_sort(a):
    if len(a) <= 1:
        return a

    pivot = a[0]
    left = []
    right = []
    for i in range(1, len(a)):
        if a[i] < pivot:
            left.append(a[i])
        else:
            right.append(a[i])

    return Quick_sort(left) + [pivot] + Quick_sort(right)



'''
병합 정렬

배열을 좌, 우로 나누고 나눈 배열을 정렬해서 다시 붙이는 과정을 방법(재귀)
분할 정복(divide and conquer) 알고리즘 중 하나
시간 복잡도 = O(nlogn)
'''
def Merge_sort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = Merge_sort(a[:mid])
    right = Merge_sort(a[mid:])

    return Merge(left, right)


def Merge(left, right):
    sort = []
    left_idx, right_idx = 0, 0

    # left, right 배열 둘다 값이 있을 때
    while len(left) > left_idx and len(right) > right_idx:
        if left[left_idx] > right[right_idx]:
            sort.append(right[right_idx])
            right_idx += 1
        else:
            sort.append(left[left_idx])
            left_idx += 1

    # left 배열에만 값이 있을 때
    while len(left) > left_idx and len(right) <= right_idx:
        sort.append(left[left_idx])
        left_idx += 1

    # right 배열에만 값이 있을 때
    while len(left) <= left_idx and len(right) > right_idx:
        sort.append(right[right_idx])
        right_idx += 1

    return sort


'''
힙 정렬

완전 이진 트리의 일종, 최대 힙과 최소 힙 두 종류가 있으며 
최대 힙은 부모 노드의 키가 자식 노드의 키보다 항상 큰 힙(max heap) - 내림차순 정렬
최소 힙은 부모 노드의 키가 자식 노드의 키보다 항상 작은 힙(min heap) - 오름차순 정렬
최소 힙의 삽입은 맨 마지막 노드에 삽입해서 부모 노드들과 비교하면서 정렬
최소 힙의 삭제는 루트를 삭제하고 루트를 맨 마지막 노드로 채우고 다시 정렬
루트 노드의 인덱스는 1
시간 복잡도 = O(nlogn)
'''
def Heap_sort(a):
    n = len(a)
    a = [0] + a

    # 힙 생성(삽입)
    for i in range(n, 0, -1):
        heapify(a, i, n)
        print("create: ", i, a)
    # 첫번째 노드와 마지막 노드 바꿔주고 다시 힙정렬 만들어줌
    res = []
    for i in range(n, 0, -1):
        res.append(a[1])
        print(a)
        a[1], a[i] = a[i], a[1]
        heapify(a, 1, i-1)
        print(i, a)

    return res


# 힙 성질을 만족하는지
def heapify(arr, idx, n):
    left_child = 2 * idx
    right_child = 2 * idx + 1
    s_idx = idx

    if left_child <= n and arr[s_idx] > arr[left_child]:
        s_idx = left_child
    if right_child <= n and arr[s_idx] > arr[right_child]:
        s_idx = right_child
    if s_idx != idx:
        arr[s_idx], arr[idx] = arr[idx], arr[s_idx]

        return heapify(arr, s_idx, n)


'''
셀 정렬

삽입 정렬과 비슷하지만, 삽입 정렬과 다르게 전체 리스트를 한번에 정렬하지 않는다
정렬할 리스트에서 간격(gap)에 따라 gap개의 부분 리스트로 나누고 각 부분 리스트를 삽입 정렬을 이용해 정렬
다시 전체 리스트로 합치고, gap을 절반으로 줄여 다시 부분 리스트를 나눈다.
부분 리스트 개수가 1개가 될 때 까지 반복 
시간 복잡도 : O(n^2)
'''
def Shell_sort(a):
    n = len(a)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            key = a[i]
            idx = i - gap
            while idx >= 0 and a[idx] > key:
                a[idx + gap] = a[idx]
                idx -= gap
            a[idx + gap] = key

        gap //= 2

    return a



array = [8, 14, 2, 5, 1, 10]
print(Heap_sort(array))