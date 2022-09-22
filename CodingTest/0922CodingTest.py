# truck         w               result
# [1,4,5,2,4]   [2,4,4,3,2]     [2,3,5,-1,2]
# [2,7,4,9]     [7,6,8]         [2,4,-1]

def solution(truck, w) :
    answer = []
    for weight in w :
        for i in range(len(truck)) :
            if weight <= truck[i] :
                answer.append(i+1)
                truck[i] -= weight
                break
        else :
            answer.append(-1)
    return answer




truck1 = [1,4,5,2,4]
w1 = [2,4,4,3,2]

truck2 = [2,7,4,9]
w2 = [7,6,8]

print(solution(truck1, w1))
print(solution(truck2, w2))

