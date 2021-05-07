import sys
sys.setrecursionlimit(1000000)

def dfs(node) :
    visited[node] = True
    for j in graph[node] :
        if not visited[j] :
            dfs(j)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1) :
    if not visited[i] :
        dfs(i)
        count+=1

print(count)