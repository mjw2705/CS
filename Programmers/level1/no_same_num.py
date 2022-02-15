arrs = [1,1,3,3,0,1,1], [4, 4, 4, 3, 3]

for arr in arrs:
    
    s = arr[0]
    answer = [s]
    for a in arr[1:]:
        if a == s:
            continue
        else:
            s = a
            answer.append(a)
            
    print(answer)