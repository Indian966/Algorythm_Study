# T = int(input())
# arr = [int(input()) for _ in range(T)]

def dp(m) :
    memo = [0]
    memo.append(1)
    memo.append(2)
    memo.append(4)


    if m > 3 :
        for _ in range(4, m + 1):
            memo.append(0)
        for i in range(4, m + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]

    print(memo[m])

# for n in arr:
#     dp(n)
dp(7)


# dp(1) = 1, dp(2) = 2, dp(3) = 1+1+1,1+2,2+1,3 = 4
# dp(4) = 7 = dp(3) + 3, dp(5) = 13 = dp(4) + dp(3) + dp(2)
# dp(6) = 24 = dp(5) + dp(4) + dp(3), dp(7) = 44
# 1 2 4 7 13 24 44