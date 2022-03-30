peoples = [70, 50, 80, 50], [70, 80, 50], [40, 50, 150, 160], [100,500,500,900,950]
limits = 100, 100, 200, 1000

from collections import deque

for people, limit in zip(peoples, limits):
    
    answer = 0
    sort_people = deque(sorted(people))
    print(sort_people)

    while sort_people:
        if len(sort_people) == 1:
            answer += 1
            break
        if sort_people[0] + sort_people[-1] <= limit:
            sort_people.popleft()
            sort_people.pop()
            answer += 1
        else:
            sort_people.pop()
            answer += 1
        print(sort_people)

    print(answer)

