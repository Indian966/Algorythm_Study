# 삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때,
# 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

# triangle	                                                result
# [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	30

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
def solution(triangle):
    answer = 0
    index = 0
    dp = [0]
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0 :
                temp = triangle[i][j] + dp[index-i]
                dp.append(temp)
            elif j == (len(triangle[i])-1) :
                temp = triangle[i][j] + dp[index-i-1]
                dp.append(temp)
            else :
                temp = triangle[i][j] + max(dp[index-i],dp[index-i-1])
                dp.append(temp)
    answer = max(dp)
    return answer

print(solution(triangle))