stringss = ["sun", "bed", "car"], ["abce", "abcd", "cdx"]
ns = 1, 2

for strings, n in zip(stringss, ns):
    print(sorted(strings, key=lambda x:(x[n], x)))