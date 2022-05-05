# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면
#    J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.


priority = [1, 1, 9, 1, 1, 1]
location = 0

from collections import deque

def solution(priorities, location):
    answer = 0
    q= deque([(number,i) for i,number in enumerate(priorities)])
    while len(q):
        item = q.popleft()

        if q and max(q)[0] > item[0]:
            q.append(item)
        else:
            answer+=1
            if item[1] == location :
                break

    return answer

print(solution(priority,location))