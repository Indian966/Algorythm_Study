# n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다.
# 권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면
# A 선수는 B 선수를 항상 이깁니다. 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다.
# 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.
#
# 선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때
# 정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.

n = 5
result = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
# result = [[1,2], [2,3]]
# return 2


def solution(n, result):
    answer = 0
    graph = [[None for _ in range(n)] for _ in range(n)]

    for win, lose in result:
        graph[win - 1][lose - 1] = True
        graph[lose - 1][win - 1] = False

    # Floyd-Warshell Algorithm
    for i in range(n):
        for j in range(n):
            for k in range(n):
                # 자기 자신일때
                if graph[j][i] == None:
                    continue

                if graph[j][i] == graph[i][k]:
                    graph[j][k] = graph[j][i]
                    graph[k][j] = not graph[j][i]

    for i in range(n) :
        # 자기 자신을 제외하고 None이 있으면 순위를 알 수 없음
        if None in graph[i][:i] + graph[i][i+1:] :
            continue
        answer+=1

    return answer

# print(solution(n,result))

from collections import defaultdict
# 집합을 이용
def another_solution(n, results) :
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)

    for result in results :
        win[result[0]].add(result[1])
        lose[result[1]].add(result[0])
    # win : defaultdict(<class 'set'>, {4: {2, 3}, 3: {2}, 1: {2}, 2: {5}})
    # lose : defaultdict(<class 'set'>, {3: {4}, 2: {1, 3, 4}, 5: {2}})

    for i in range(1, n+1) :
        # i번 선수에게 진 사람은 i번 선수를 이긴 사람에게도 진다는 원리
        for winner in lose[i] :
            win[winner].update(win[i])
        for loser in win[i] :
            lose[loser].update(lose[i])
    # win : defaultdict(<class 'set'>, {4: {2, 3, 5}, 3: {2, 5}, 1: {2, 5}, 2: {5}, 5: set()})
    # lose : defaultdict(<class 'set'>, {3: {4}, 2: {1, 3, 4}, 5: {1, 2, 3, 4}, 1: set(), 4: set()})

    for i in range(1, n+1) :
        if len(win[i]) + len(lose[i]) == n - 1 : answer += 1

    return answer

print(another_solution(n,result))