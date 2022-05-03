# 3
# 26 40 83
# 49 60 57
# 13 89 99

N = int(input())
data = []
for _ in range(N) :
    data.append(list(map(int,input().split())))
dp = [[100, 100, 100] for _ in range(N)]
for i in range(3) :
    dp[0][i] = data[0][i]
# index = data[i].index(min(data[i]))
for i in range(1,N) :
    for j in range(3):
        if j == 0 :
            dp[i][0] = data[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        elif j == 1 :
            dp[i][1] = data[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        else :
            dp[i][2] = data[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[N-1]))
