# 각 건물에서 보이는 자신보다 크거나 같은 건물들의 수를 모두 합한 값
# heights = [1,4,2,5,3]
# heights = [3, 5, 4, 2, 4, 4, 6, 5]   #result 6
# heights = [5,5,5]

def solution (heights) :
    answer = 0

    def left_search(index) :
        flag = heights[index]
        count = 0
        for i in range(index-1,-1,-1) :
            if heights[i] >= flag:
                count += 1
                flag = heights[i] + 1
        return count

    def right_search(index) :
        flag = heights[index]
        count = 0
        for i in range(index+1, len(heights)) :
            if heights[i] >= flag :
                count+=1
                flag= heights[i] + 1
        return count


    for i in range(len(heights)) :
        answer += left_search(i) + right_search(i)

        # if i == 0 :
        #     answer += right_search(0)
        #     print(i, answer)
        # elif i == len(heights)-1 :
        #     answer += left_search(len(heights)-1)
        #     print(i, answer)
        # else:
        #     answer += right_search(i) + left_search(i)
        #     print(i, answer)

    return answer

print(solution(heights))
