# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5
#
# 5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
# 이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중
# N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

# N	number	return
# 5	12	    4
# 2	11	    3

def solution(N, number):
    answer = -1
    dp  =[set([N*int('1'*i)]) for i in range(1, 9)]
    for i in range(8) :
        for j in range(i):
            for num1 in dp[j]:
                for num2 in dp[i - j - 1]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
        if number in dp[i] :
            return i+1

    return answer

print(solution(5,12))