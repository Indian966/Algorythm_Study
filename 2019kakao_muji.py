def solution(food_times, k):
    answer = 0
    time = 0
    cir_time = len(food_times)
    n = k / cir_time
    # for i in range(0, int(n)):
    #     for food in food_times:
    #         # print(food)
    #         if food > 0:
    #             food = food - 1
    #             print(food)
    i = 0
    j = 0
    while answer < 1:
        if i >= len(food_times):
            i = 0
        elif j >= k:
            answer = i
            break
        else:
            if food_times[i] > 0:
                food_times[i] -= 1
                i += 1
                j += 1
            else : i+=1

    return answer

food_times = [3,1,2]
k = 5
print(solution(food_times, k))