# N = int(input())


def coin_charge (n) :
    money = [0]
    coin = [3, 5]
    for i in range(1,n+1) :
        money.append(N)
    for i in range(len(coin)) :
        for j in range(coin[i], n+1) : #n:18 coin[i] => 5
            money[j] = min(money[j], money[j - coin[i]] + 1)
    if money[-1] == N:
        return -1
    else:
        return money[-1]

for N in range(3,5000) :
    if coin_charge(N) < 0:
        print(N)