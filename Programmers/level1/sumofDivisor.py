ns = 12, 5, 1, 2

for n in ns:

    prime = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            pair = n // i
            prime.extend([i, pair])
    
    print(sum(set(prime)))