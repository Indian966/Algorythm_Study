#N = int(input())
N = 8


def coin_charge (n) :
    memo = [0 for _ in range(n+1)]
    for i in range(2,n+1) :
        memo[i] = memo[i-1]+1
        if not i % 2 :
            memo[i] = min(memo[i], memo[i//2]+1)
        if not i % 3 :
            memo[i] = min(memo[i], memo[i//3]+1)
    print(memo[-1])
coin_charge(N)
