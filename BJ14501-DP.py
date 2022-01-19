day = int(input())
cost = []
pay = []
dp = []
for i in range(day):
    N, M = map(int, input().split())
    cost.append(N)
    pay.append(M)
    dp.append(M)
dp.append(0)

for i in range(day - 1, -1, -1):
    if cost[i] + i > day:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], pay[i] + dp[i + cost[i]])
print(dp[0])