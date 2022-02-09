sizess = [[60, 50], [30, 70], [60, 30], [80, 40]], [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]], [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

for sizes in sizess:
    
    size_w = max(max(x) for x in sizes)
    size_h = max(min(x) for x in sizes)

    answer = size_w * size_h