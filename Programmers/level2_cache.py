cacheSize = 0
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
# cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]


def solution(cacheSize, cities):
    cache = []
    time = 0
    for city in cities:
        city = city.lower()
        if cacheSize == 0:
            time += 5
        else:
            if city in cache:
                cache.pop(cache.index(city))
                cache.append(city)
                time += 1
            else:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
                time += 5
    return time


print(solution(cacheSize, cities))