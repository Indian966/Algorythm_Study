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
def time_convert(time_list) :
    # time_list : 한 명이 일 할 수 있는 시간 리스트
    for i in range(len(time_list)) :
        if ';' in time_list[i] :
            arr1, arr2 = time_list[i].split(';')
            work = time_calc(arr1) + time_calc(arr2)
            print(work)
        else :
            work = time_calc(time_list[i])
            print(work)




def time_calc (arr: list) :
    # arr : 하루에 일 할 수 있는 시간

    small, big = arr.split('~')
    answer = list(range(int(small[1]), int(big[1])))

    # [0, 1, 2, 3]
    return answer

# time_convert(a_time)

# week_dict = {
#     'Mon' : [0, 0, 0, 0, 0, 0, 0, 0],
#     'Tue' : [0, 0, 0, 0, 0, 0, 0, 0],
#     'Wen' : [0, 0, 0, 0, 0, 0, 0, 0],
#     'Thu' : [0, 0, 0, 0, 0, 0, 0, 0],
#     'Fri' : [0, 0, 0, 0, 0, 0, 0, 0]
#     }

week_list = [[0] * (8) for _ in range(5)]
pprint(week_list)
time_convert(a_time)