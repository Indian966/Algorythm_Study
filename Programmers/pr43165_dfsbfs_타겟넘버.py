# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때
# 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.
# numbers	        target	return
# [1, 1, 1, 1, 1]	3	    5
# [4, 1, 2, 1]	    4	    2

from collections import deque


numbers = [1, 1, 1, 1, 1]
target = 3
def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((0,0))
    while q :
        number, l = q.popleft()
        if l > len(numbers) :
            break
        if l == len(numbers) and number == target :
            answer+=1
        q.append((number + numbers[l - 1], l + 1))
        q.append((number - numbers[l - 1], l + 1))

    return answer
print(solution(numbers,target))