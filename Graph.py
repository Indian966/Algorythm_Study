

# def dfs(graph,visit,count, start_node):
#     visit.append(start_node)
#     N=len(graph)
#     for i in range(1,N) :
#         if i not in visit and graph[start_node][i]:
#             dfs(graph,visit,count,i)
#             count+=1
#     return count

T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())
    graph = [[0] * N for _ in range(N)]
    count = 0
    for a in range(M) :
        start, end = map(int, input().split())
        graph[start-1][end-1] = 1
        graph[end-1][start-1] = 1
    for i in range(N) :
        for j in range(i+1, N ):
                for k in range(j+1, N ):
                    if graph[i][j] and graph[j][k] and graph[k][i]:
                        count += 1
    print("#{} {}".format(tc, count))
# 0 1 1
# 1 0 1
# 1 1 0