genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

from collections import defaultdict

def solution(genres, plays):
    classify_genres = defaultdict(list)
    for i in range(len(genres)):
        classify_genres[genres[i]].append([i, plays[i]])

    genre_list = []
    for genre in classify_genres:
        classify_genres[genre].sort(key=lambda x:x[1], reverse=True)
        genre_list.append([genre, sum([nums for _, nums in classify_genres[genre]])])
    genre_list.sort(key=lambda x: x[1], reverse=True)

    answer = []
    for g in genre_list:
        for idx in classify_genres[g[0]][:2]:
            answer.append(idx[0])
            
    return answer