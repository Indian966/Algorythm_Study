# N = int(input())
N = 4
cards = [1, 5, 6, 7]

class MinGyu(object) :
    def __init__(self, n, v):
        self.number = n
        self.value = v

    def getNumber(self):
        return self.number

    def getValue(self):
        return self.value

    def density(self): # 가중치
        return self.getValue()/self.getNumber()

def dp (N) :
    memo = []
    ans = [[0 for x in range(N + 1)] for x in range(N + 1)]
    for i in range(N) :
        memo.append(MinGyu(N,cards[i]))
    memo.sort(key=MinGyu.density)
    for j in memo :
        print(j.value)
dp(N)

# density
# [0.25, 1.25, 1.5, 1.75]