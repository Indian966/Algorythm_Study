# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때,
# 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

import math
from itertools import permutations

numbers = "1231"
def solution(numbers):
    answer = 0

    def primenumber(x):
        for i in range(2, int(math.sqrt(x) + 1)):
            if (x % i) == 0:
                return False
        if x == 1 or x == 0:
            return False
        return True

    numbers = list(numbers)

    arr = set()
    for m in numbers :
        arr.add(int(m))
    print(arr, numbers)
    for k in range(1,len(numbers)+1) :
        print(k)
        result = list(permutations(numbers, k))
        print(result)
        for i in result:
            print(i)
            string = ''
            for j in range(len(i)):
                string += str(i[j])
            print(string)
            arr.add(int(string))


    print(arr)
    for n in arr :
        if primenumber(n) :
            print(n)
            answer+=1
    return answer

print(solution(numbers))