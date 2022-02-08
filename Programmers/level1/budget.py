ds = [1,3,2,5,4], [2, 2, 3, 3]
budgets = 9, 10

for d, budget in zip(ds, budgets):

    answer = 0
    sorting = sorted(d)
    for s in sorting:
        budget -= s
        if budget < 0:
            break
        answer += 1
    print(answer)
