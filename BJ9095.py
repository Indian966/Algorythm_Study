#T = int(input())
n = 4


def dp(m) :
    memo = [0 for _ in range(m + 1)]
    coin = [1,2,3,4]


# dp(1) = 1, dp(2) = 2, dp(3) = 1+1+1,1+2,2+1,3 = 4
# dp(4) = 7 = dp(3) + 3, dp(5) = 13 = dp(4) + dp(3) + dp(2)
# dp(6) = 24 = dp(5) + dp(4) + dp(3), dp(7) = 44
1 2 4 7 13 24 44