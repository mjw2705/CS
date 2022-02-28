ns = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12


for n in ns:
    nums = ['1', '2', '4']
    answer = ''
    rest = []
    while n > 0:
        if n % 3 == 0:
            answer += '4'
            n = n // 3 - 1
        else:
            answer += nums[n % 3 - 1]
            n = n // 3
    print(answer[::-1])
