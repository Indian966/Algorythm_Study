# N = int(input())


def my_solution(N) :
    dp = [0]

    for i in range(1, N + 1):
        if i == 1:
            dp.append(9)
        else:
            dp.append((dp[i - 1] * 2) - (i - 1))

    print(dp[-1] % 1000000000)


def solution(N) :
    dp = [[0]*10 for _ in range(N+1)]
    for i in range(1,10) :
        dp[1][i] = 1

    for i in range(2,N+1) :
        for j in range(10) :
            if j == 0 :
                dp[i][j] = dp[i-1][1]
            elif j == 9 :
                dp[i][j] = dp[i-1][8]
            else :
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    print(sum(dp[N]) % 1000000000)


for N in range(1, 15) :
    solution(N)
    my_solution(N)

