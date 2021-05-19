import sys

N = int(input())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

def calc (array) :
    sum = 0
    for i in array:
        if sum + 1 < i:
            return sum + 1
        sum += i
    return sum + 1

print(calc(array))

# 3 1 6 2 7 30 1 = 50
# N - 가장 무거운 추 = 나머지
# 50 - 30 = 20
# sum + 1 = 측정 못하는 값
# 1 1 1 가장 극단적인 예