# 입국심사를 기다리는 사람 수 n,
# 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때,
# 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.
time = [3, 5, 9, 2, 7, 1]
n = 24
def solution(n, times):
    answer = 0
    left , right = 1, max(times) * n
    while left <= right :
        mid = (left + right) // 2
        count = 0
        for i in times :
            count += mid // i
            if count >= n :
                answer = mid
                right = mid -1
                break
        if count < n :
            left = mid + 1
    return answer

print(solution(n, time))