# Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때,
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

scoville = [1, 2, 3, 9, 10, 12]
K = 7
# return 2

import heapq

def solution(scoville, K):
    answer = 0
    q = scoville
    heapq.heapify(q)
    while len(q) >= 2 :
        if q[0] >= K or len(q) < 2 :
            break
        first = heapq.heappop(q)
        second = heapq.heappop(q)
        heapq.heappush(q, first + (second * 2))
        answer+=1
    if q[0] < K :
        return -1
    else:
        return answer

print(solution(scoville,K))