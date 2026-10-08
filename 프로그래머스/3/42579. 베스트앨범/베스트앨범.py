def solution(genres, plays):
    answer = []
    
    albums = {}
    total = {}
    
    for i in range(len(genres)):
        total[genres[i]] = total.get(genres[i], 0) + plays[i]
        albums[genres[i]] = albums.get(genres[i], []) + [(plays[i], i)]
    
    totalSort = sorted(total.items(), key=lambda x: x[1], reverse=True)
    
    for (genre, totalPlay) in totalSort:
        albums[genre] = sorted(albums[genre], key=lambda x: (-x[0], x[1]))
        print(albums)
        answer += [idx for (play, idx) in albums[genre][:2]]
    
    return answer