ns = 3, 4

for n in ns:

    s = "수박"
    a, b = divmod(n, 2)
    if b == 0 :
        answer = s * a
    else:
        answer = s * a + s[0]