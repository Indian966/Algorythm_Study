
# 4 6
# 101111
# 101010
# 101011
# 111011

n, m = map(int, input().split())
graph = []
for _ in range(n) :
    temp = list(map(int,input()))
    graph.append(temp)

visited = [[0] * m for _ in range(n)]

dr = [0, 0, -1, 1] #위로가기
dc = [-1, 1, 0, 0] #아래로가기

arr = []
arr.append((0,0))
visited[0][0] = 1

while arr :
    a,b = arr.pop(0)
    if a == n - 1 and b == m - 1 :
        print(visited[a][b])
        break
    for i in range(4) :
        ax = a + dr[i]
        by = b + dc[i]
        if ax >= 0 and ax < n and by >= 0 and by < m :
            if visited[ax][by] == 0 and graph[ax][by] == 1 :
                visited[ax][by] = visited[a][b] + 1
                arr.append((ax,by))