# BruteForce

day = int(input())
schedule = []
graph = [0 for _ in range(day)]
for i in range(day):
    N, M = map(int, input().split())
    schedule.append([i,N,M])


schedule.sort(key=lambda x: x[2]/x[1], reverse=True)
sum = 0
for i in schedule :
    print(i)
    if (i[0] + i[1]) <= day:
        if graph[i[0]] == 0 and graph[i[0]+i[1]-1] == 0 :
            for j in range(i[0], i[0] + i[1]):
                graph[j] = 1
            sum += i[2]
            print(graph)

print(sum)
