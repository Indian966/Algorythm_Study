# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록
# solution 함수를 작성해주세요.
# numbers	return
# [6, 10, 2]	"6210"
# [3, 30, 34, 5, 9]	"9534330"
from itertools import permutations
numbers = [6, 10, 2]

def solution(numbers):
    per = list(permutations(numbers, len(numbers)))
    result = []
    for i in per :
        temp = ''
        for j in i :
            temp+=str(j)
        result.append(temp)
    result.sort()

    return result[-1]

print(solution(numbers))