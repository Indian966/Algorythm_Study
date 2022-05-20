# prices	        return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]

from collections import deque

prices = [1, 1, 0]
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices :
        item = prices.popleft()
        if not prices :
            answer.append(0)
        else :
            time = 0
            for next in prices :
                if item <= next :
                    time +=1
                else :
                    time+=1
                    break
            answer.append(time)
    return answer

print(solution(prices))