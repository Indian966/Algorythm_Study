# 격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다.
# 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를
# 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.

# m	n	puddles	    return
# 4	3	[[2, 2]]	4

m = 4
n = 3
puddles = [[2,2]]

def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1

    for i in range(1,n+1) :
        for j in range(1,m+1) :
            if i==1 and j==1 : continue
            if [j,i] in puddles :
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
    return dp[n][m]

print(solution(m,n,puddles))
