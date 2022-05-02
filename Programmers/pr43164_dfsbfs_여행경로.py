# 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.
# 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때,
# 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
from collections import defaultdict
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# return ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
# 다음 경로가 없다면 리스트에 저장해서 거꾸로 뒤집음
def solution(tickets):
    answer = []
    dict = defaultdict(list)

    for ticket in tickets :
        dict[ticket[0]].append(ticket[1])
    print(dict)

    for key in dict.keys() :
        dict[key].sort(reverse=True)
    print(dict)

    q = ['ICN']
    while q:
        airport = q[-1]
        # 다음 목적지로의 티켓이 없을 경우
        if not dict[airport] :
            answer.append(q.pop())
        else:
            q.append(dict[airport].pop())
    answer.reverse()
    return answer

print(solution(tickets))