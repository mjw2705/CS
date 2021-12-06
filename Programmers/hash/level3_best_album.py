from collections import defaultdict

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


answer = []
playnum_dict = defaultdict(int)
genre_dict = defaultdict(list)

for i in range(len(genres)):
    playnum_dict[genres[i]] += plays[i]
    genre_dict[genres[i]].append([i, plays[i]])

playnum_dict = sorted(playnum_dict.items(), key=lambda x:x[1], reverse=True)

for i in genre_dict:
    genre_dict[i] = sorted(genre_dict[i], key=lambda x:(-x[1], x[0]))

for i in range(len(playnum_dict)):
    if len(genre_dict[playnum_dict[i][0]]) > 1:
        answer += [idx for idx, num in genre_dict[playnum_dict[i][0]][:2]]
    else:
        answer += [genre_dict[playnum_dict[i][0]][0][0]]

print(answer)



from collections import defaultdict

def solution(genres, plays):
    answer = []
    playnum_dict = defaultdict(int)
    genre_dict = defaultdict(list)

    for i in range(len(genres)):
        playnum_dict[genres[i]] += plays[i]
        genre_dict[genres[i]].append([i, plays[i]])

    playnum_dict = sorted(playnum_dict.items(), key=lambda x: x[1], reverse=True)

    for i in genre_dict:
        genre_dict[i] = sorted(genre_dict[i], key=lambda x: (-x[1], x[0]))

    for i in range(len(playnum_dict)):
        if len(genre_dict[playnum_dict[i][0]]) > 1:
            answer += [idx for idx, num in genre_dict[playnum_dict[i][0]][:2]]
        else:
            answer += [genre_dict[playnum_dict[i][0]][0][0]]


    return answer