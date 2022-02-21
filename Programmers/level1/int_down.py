n = 118372

arr = sorted(list(str(int(n))), reverse=True)
answer = int(''.join(arr))
print(answer)