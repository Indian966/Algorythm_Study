# Knapsack Problem
# [[0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10],
# [0, 0, 20, 20, 20, 20, 20, 30, 30, 30, 30, 30],
# [0, 0, 20, 20, 20, 25, 25, 30, 30, 30, 35, 35],
# [0, 0, 20, 20, 20, 25, 27, 30, 30, 32, 35, 37],
# [0, 0, 20, 20, 20, 25, 27, 30, 31, 32, 35, 37]]
W = 12
N = 5
items = [["camera", 5, 10], ["smartphone", 2, 20], ["cup", 3, 5], ["towel", 4, 7], ["pants", 6, 11]]


# result = [[12, 37, 3], [“camera”, “smartphone”, “towel”]]

#   가방의 무게보다 물건이 무거우면 넣지 않음
#   현재 배낭의 가치 (dp[i-1][j]) vs 이 물건을 넣고 이 물건 만큼 무게를 뺐을 때의 가치(items[i] + dp[i-1][j-weight])
#   dp[i][j] = max(dp[i-1][j], items[i] + dp[i-1][j-weight])


def solution(W, N, items):
    answer = []

    dp = [[0] * (W) for _ in range(N)]

    for i in range(N):
        for j in range(W):
            weight = items[i][1]
            value = items[i][2]

            # 현재 가방 무게가 물건보다 가벼우면
            if j < weight:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], value + dp[i - 1][j - weight])
    res = dp[i][j]
    print(dp)
    # 정답 출력 용
    result = dp[i][j]

    # back tracking
    w = W - 1
    name = []
    for i in range(N, 0, -1):
        if res <= 0:
            break
        if res == dp[i - 1][w]:
            continue
        else:  # 현재 가방의 가치가 이전 물건의 가치보다 높다면
            name.append(items[i - 1][0])

            res = res - items[i - 1][2]
            w -= items[i - 1][1]
    info = [W, result, len(name)]
    answer = [info, name]

    return answer


print(solution(W, N, items))