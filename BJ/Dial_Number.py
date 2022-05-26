import sys

T = int(input())
for _ in range(1, T+1) :
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(sys.stdin.readline().strip())
    numbers.sort()
    answer = 0
    for i in range(len(numbers)-1):
        if numbers[i] in numbers[i+1]:
            answer += 1

    if answer>0 :
        print('NO')
    else: print('YES')