# 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때,
# 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# return 3


def solution(n, edge):
    start, answer = 0
    visited = [0] * n
    queue = []
    edge.sort(key=lambda x:x[0])
    def bfs (start) :
        queue.append(start)
        while queue :
            s = queue.pop(0)
            if visited[s] == 0 :
                visited[s] = 1
            for index in range(len(edge)) :
                if s in edge[index] and visited[index] == 0 :
                    queue.append(index)



    return answer