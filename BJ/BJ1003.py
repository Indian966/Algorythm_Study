T = int(input())
arr = [int(input()) for _ in range(T)]

def zero(n) :
    memo = []
    memo.append(1)
    memo.append(0)
    if n <= 1:
        return memo[n]
    elif n > 1 :
        for _ in range(1, n) :
            memo.append(0)
        for i in range(2, n+1) :
            memo[i] = memo[i-1] + memo[i-2]
    return memo[-1]

def one(n) :
    memo = []
    memo.append(0)
    memo.append(1)
    if n <= 1 :
        return memo[n]
    elif n > 1 :
        for _ in range(1, n) :
            memo.append(0)
        for i in range(2, n+1) :
            memo[i] = memo[i-1] + memo[i-2]
    return memo[-1]


for n in arr :
    answer = ''
    answer = str(zero(n)) + ' ' + str(one(n))
    print(answer)

# 1
# 0 1
# 2
# 1 1
# 3
# 1 2
# 4
# 2 3
# 5
# 3 5
# 6
# 5 8
# 7
# 8 13
# 8
# 13 21
# 9
# 21 34
# 10
# 34 55
# 11
# 55 89
# 12
# 89 144
# 13
# 144 233