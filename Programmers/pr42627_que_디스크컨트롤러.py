#  작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는
#  방법으로 처리하면
#  평균이 얼마가 되는지
jobs = [[0, 3], [1, 9], [2, 6]]
import heapq
def solution(jobs):
    answer = 0
    total = 0
    front_time = -1
    cur_time = 0
    process = []
    while total < len(jobs):
        for task in jobs :
            if front_time < task[0] and task[0] <= cur_time:
                # process.append([task[0], task[1]])
                heapq.heappush(process, (task[0], task[1]))
        print(process)
        if process :
            # job = process.pop()
            job = heapq.heappop(process)
            # print(job)
            front_time = cur_time
            cur_time+=job[1]
            answer+= cur_time- job[0]
            total+=1
        else:
            cur_time+=1


    return answer//len(jobs)

print(solution(jobs))

import heapq


def another_solution(jobs):
    answer, cnt_time, i = 0, 0, 0
    # 가장 최근에 처리한 작업의 처리 시작 시간
    start = -1
    # 요청이 들어온 작업들을 담아두는 최소 힙
    process = []

    # 모든 작업 처리할 때 까지 반복
    while i < len(jobs):

        for job in jobs:
            if start < job[0] <= cnt_time:
                heapq.heappush(process, (job[1], job[0]))

        if process:
            job = heapq.heappop(process)
            start = cnt_time
            cnt_time += job[0]
            answer += cnt_time - job[1]
            i += 1
        else:
            cnt_time += 1

    return answer // len(jobs)