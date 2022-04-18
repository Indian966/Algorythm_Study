# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때,
# 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

#n=3
computers = [[1,1,0], [1,1,0], [0,0,1]]

def solution (n, computers) :
    answer = 0
    start = 0
    queue = []
    visited = [False] * n
    def bfs (start) :
        queue.append(start)
        while queue :
            s = queue.pop(0)
            if visited[s] == False :
                visited[s] = True
            for i in range(n) :
                if computers[s][i] == True and visited[i] == False :
                    queue.append(i)
    while 0 in visited :
        answer+=1
        bfs(visited.index(0))

    return answer

print(solution(3, computers))

def another_solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer