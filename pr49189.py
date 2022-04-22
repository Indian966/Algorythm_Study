# 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때,
# 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

from collections import deque

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# return 3


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    for s, e in edge:  # 그래프에 현재 노드와 연결되어있는 노드 저장
        graph[s].append(e)
        graph[e].append(s)

    for e in graph:
        e.sort()

    def bfs (n) :
        visited = [0 for _ in range(n+1)]
        visited[1] = 1
        q = deque()
        q.append((1, 0))  # 시작 노드, 거리


        while q:
            node, dist = q.popleft()
            for i in graph[node] :
                if visited[i] == 0 :
                    visited[i] = dist + 1
                    q.append((i, dist + 1))

        max_val = max(visited)
        return visited.count(max_val)

    return bfs(n)

print(solution(n,vertex))