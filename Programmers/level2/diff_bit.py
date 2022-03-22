numbers = [2, 7]

answer = []
for number in numbers:
    number = int(number)
    bins = '0' + bin(number)[2:]

    if number % 2 == 0:
        answer.append(int(number+1))
    else:
        idx = bins.rfind('0')
        bins = list(bins)
        bins[idx] = '1'
        bins[idx+1] = '0'
        answer.append(int(''.join(bins), 2))
    
print(answer)