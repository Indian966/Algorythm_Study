from itertools import combinations

n,m = map(int,input().split())

city = []
chicken = []
house = []
for _ in range(n) :
    city.append(list(map(int,input().split())))

for i in range(n) :
    for j in range(n) :
        if city[i][j] == 1 :
            house.append([i, j])
        elif city[i][j] == 2 :
            chicken.append([i, j])

answer = 100000
chicken_s = list(combinations(chicken, m))

result = []

for comp in chicken_s :
    chicken_dist = 0
    for c in range(len(house)) :
        dist = 10000
        for x,y in comp :
            dist = min(dist, abs(x-house[c][0])+abs(y-house[c][1]))
        chicken_dist += dist
    answer = min(answer, chicken_dist)
print(answer)