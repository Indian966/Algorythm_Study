import sys
import copy

input = sys.stdin.readline
N, M = map(int, input().strip().split())
graph = []
for i in range(N):
    L = list(map(int, input().strip().split()))
    graph.append(L)

dr = [-1, 0, 1, 0] #위로가기
dc = [0, 1, 0, -1] #아래로가기

virus_list = []
safe = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus_list.append([i,j])

def wall (start, count) :
    global safe
    if count == 3 :
        copy_graph = copy.deepcopy(graph)
        for num in range(len(virus_list)) :
            r,c = virus_list[num]
            spread_virus(r,c,copy_graph)
        safe_count = sum(i.count(0) for i in copy_graph)
        safe = max(safe, safe_count)
        return True
    else:
        for i in range(start, N * M):
            r = i // M
            c = i % M
            if graph[r][c] == 0:
                graph[r][c] = 1
                wall(i, count + 1)
                graph[r][c] = 0

def spread_virus(row, col, copy_graph):
    if copy_graph[row][col] == 2:
        for dir in range(4):
            move_row = row + dr[dir]
            move_col = col + dc[dir]
            if move_row >= 0 and move_col >= 0 and move_row < N and move_col < M:
                if copy_graph[move_row][move_col] == 0:
                    copy_graph[move_row][move_col] = 2
                    spread_virus(move_row, move_col, copy_graph)

wall(0,0)
print(safe)