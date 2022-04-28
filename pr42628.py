# 이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때,
# 모든 연산을 처리한 후 큐가 비어있으면 [0,0]
# 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.

# I 숫자	큐에 주어진 숫자를 삽입합니다.
# D 1	큐에서 최댓값을 삭제합니다.
# D -1	큐에서 최솟값을 삭제합니다.

# ["I 16","D 1"]	[0,0]
# ["I 7","I 5","I -5","D -1"]	[7,5]

import heapq

operations = ["I 7","I 5","I -5","D -1"]

def solution(operations):
    answer = []
    que = []
    for com in operations:
        command = com.split()[0]
        numb = int(com.split()[1])
        if command == 'I':
            heapq.heappush(que,numb)
        else :
            if not len(que):
                pass
            elif numb == -1:
                heapq.heappop(que)
            else :
                que = heapq.nlargest(len(que), que)[1:]
                heapq.heapify(que)

    if not que :
        answer.append(0)
        answer.append(0)
    else :
        answer.append(max(que))
        answer.append(min(que))
    return answer

print(solution(operations))