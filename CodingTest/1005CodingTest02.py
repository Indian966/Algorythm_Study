

def solution(n, m, friends, movies) :
    answer = []
    #   영화를 조합하여 중복 제거
    #   가장 많이 만족 시키는 최소한의 경우의 수
    dp = [[0] * (m) for _ in range(n)]

    for i in range(m) :
        arr = []
        for j in range(i):
            arr += movies[i]
            res = set(arr)
            dp[i][j] = len(res)
    print(dp)
    return answer

n = 10
m = 7
friends = ["a", "b", "c", "d", "e", "f", "g","h", "i", "j"]
movies = [["a", "c", "d", "h", "i", "j"],
          ["a", "d", "i"],
          ["a", "c", "f", "g", "h", "i", "j"],
          ["b", "d","g"],
          ["b", "c", "f", "h", "i"],
          ["b", "e", "g","j"],
          ["b", "c", "g", "h", "i"]]

print(solution(n,m,friends,movies))