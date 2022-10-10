"""
    1) 시간표를 만들어야 하고
    2) 알바생이 없는 시간을 최소로 줄여야하며
    3) 이번주 중 아무도 근무할 수 없는 시간을 알아내야 합니다.
    a) 단, 근무 가능한 알바생이 있으나, 10시간 초과로 근무가 불가능한 경우 아래
    방식 중 선택하여 출력 가능합니다.
    i) 아무도 근무할 수 없는 시간으로 취급
    ii) 초과 근무로 근무 불가한 시간으로 취급
"""

from pprint import pprint


a_time = ['10:00~14:00', '15:00~18:00', '11:00~13:00;14:00~16:00', '10:00~11:00', '15:00~18:00']
b_time = ['11:00~14:00', '14:00~16:00', '16:00~18:00', '10:00~11:00;12:00~13:00', '14:00~16:00']
c_time = ['14:00~16:00', '16:00~18:00', '10:00~12:00', '12:00~14:00', '14:00~16:00']
d_time = ['14:00~18:00', '10:00~18:00', '12:00~14:00', '14:00~15:00;16:00~17:00', '10:00~12:00']

# 시간을 알아 보기 쉽게 1,0으로 만들기
def time_convert(work_time) :
    # time_list : 한 명이 일 할 수 있는 시간 리스트

    def time_calc(arr: list):
        # arr : 하루에 일 할 수 있는 시간

        small, big = arr.split('~')
        answer = list(range(int(small[1]), int(big[1])))

        # [0, 1, 2, 3]
        return answer

    if ';' in work_time:
        arr1, arr2 = work_time.split(';')
        work = time_calc(arr1) + time_calc(arr2)
        return work
    else:
        work = time_calc(work_time)
        return work

week_list = [[0] * (8) for _ in range(5)]

# 시간표 작성
def time_table(week: list) :

    # a
    for day in range(len(week)) :
        work = time_convert(a_time[day])
        for i in work:
            if week[day][i] == 0:
                week[day][i] = ['a']
            else:
                week[day][i].append('a')

    # b
    for day in range(len(week)) :
        work = time_convert(b_time[day])
        for i in work:
            if week[day][i] == 0:
                week[day][i] = ['b']
            else:
                week[day][i].append('b')

    # c
    for day in range(len(week)) :
        work = time_convert(c_time[day])
        for i in work:
            if week[day][i] == 0:
                week[day][i] = ['c']
            else:
                week[day][i].append('c')

    # d
    for day in range(len(week)) :
        work = time_convert(d_time[day])
        for i in work:
            if week[day][i] == 0:
                week[day][i] = ['d']
            else:
                week[day][i].append('d')


    return week


pprint(time_table(week_list))


'''
[
    [['a'],['a', 'b'],['a', 'b'],['a', 'b'],['c', 'd'],['c', 'd'],['d'],['d']],
    [['d'],['d'],['d'],['d'],['b', 'd'],['a', 'b', 'd'],['a', 'c', 'd'],['a', 'c', 'd']],
    [['c'], ['a', 'c'], ['a', 'd'], ['d'], ['a'], ['a'], ['b'], ['b']],
    [['a', 'b'], 0, ['b', 'c'], ['c'], ['d'], 0, ['d'], 0],
    [['d'], ['d'], 0, 0, ['b', 'c'], ['a', 'b', 'c'], ['a'], ['a']]
]
[
    [['a'],[],[],[],[],[],['d'],['d']],
    [['d'],['d'],['d'],['d'],[],[],[],[]],
    [['c'], [], [], ['d'], ['a'], ['a'], ['b'], ['b']],
    [[], 0, [], ['c'], ['d'], 0, ['d'], 0],
    [['d'], ['d'], 0, 0, [], [], ['a'], ['a']]
]
10시간 카운팅 - 1명만 일 할 수 있는 시간대 우선 카운트 
4시간 근무 가능하지만 2시간만 일하는 현상,
'''
def solo_worker (worker : str) :
    work_time = 10
    for day in range(len(week_list))  :
        for hour in range(len(week_list[day])) :
            if week_list[day][hour] != 0 and len(week_list[day][hour]) > 0 and worker in week_list[day][hour]:
                if work_time == 0:
                    week_list[day][hour] = ['over 10 hours']
                else :
                    work_time-=1

    return worker, work_time

solo_worker('a')
solo_worker('b')
solo_worker('c')
solo_worker('d')
pprint(week_list)