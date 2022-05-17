from collections import deque

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
# return 2

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    cur_time = 0
    bridge = [0] * bridge_length
    bridge_weight = 0
    while bridge :
        cur_time+=1
        bridge_weight -= bridge[0]
        bridge.pop(0)
        if truck_weights :
            if bridge_weight + truck_weights[0] <= weight :
                bridge_weight += truck_weights[0]
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)

    return cur_time

print(solution(bridge_length, weight, truck_weights))