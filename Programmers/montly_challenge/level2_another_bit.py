numbers = [2,7]

def f(num):
    if num % 2 == 0:
        return num + 1
    else:
        num_bin = bin(num)[2:]
        print(num_bin)

answer = [f(num) for num in numbers]
print(answer)