# 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다.
# 노래의 장르를 나타내는 문자열 배열 genres와
# 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
# 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
# return [4, 1, 3, 0]

def solution(genres, plays):
    answer = []
    chart = {}
    for i in range(len(genres)) :
        name = genres[i]
        if name in chart :
            chart[name].append((i, plays[i]))
        else :
            chart[name] = [(i, plays[i])]

    genres_sorted = []
    for key in chart.keys() :
        genres_sorted.append((key, sum([x[1] for x in chart[key]])))
    genres_sorted = sorted(genres_sorted, key= lambda x: -x[1])
    # print('genres_sorted : ',genres_sorted)

    for key, _ in genres_sorted :
        musics = sorted(chart[key], key= lambda x: -x[1])
        # print(musics)
        for item in musics[:2] :
            answer.append(item[0])

    return answer

print(solution(genres,plays))