n = int(input())
graph = []
for _ in range(n) :
    temp = list(map(int,input().split()))
    graph.append(temp)

print(n, graph)

for i in graph :
    if 9 in i :
        x = graph.index(i)
        y = i.index(9)

print(x,y)

size = 2
time = 0
list = []
for i in range(n):
    for j in range(n):
        if graph[i][j] > 0 and graph[i][j] < size :
            dist = abs(x-i) + abs(y-j)
            list.append([i,j,dist])
list_index = 0
list.sort(key=lambda x : x[2])
cnt = 0
while list_index <= len(list) :
    i, j = list[list_index][0], list[list_index][1]
    if size > graph[i][j] :
        cnt+=1
        time+=list[list_index][2]




print(list)
# fish = 0
# if fish < size :
