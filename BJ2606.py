import sys
# node = int(input())
# pair = int(input())
# graph = []
# for _ in range(node) :
#     n, m = map(int, input())

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

adj = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(N+1):
    adj[i].sort()
print(adj)
visited = [0 for _ in range(N+1)]

stack = [1]
result = []

while stack :
    current = stack.pop()
    if visited[current] == 0 :
        result.append(current)
        visited[current] = 1
        stack += reversed(adj[current])


print(len(result)-1)


