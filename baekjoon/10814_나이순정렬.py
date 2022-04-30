N = 3
member = ['21 Junkyu', '21 Dohyun', '20 Sunyoung']

mems = []
for mem in member:
    age, name = mem.split(' ')
    mems.append((age, name))

sort_mem = sorted(mems, key=lambda x:x[0])
for sorts in sort_mem:
    print(sorts[0], sorts[1])