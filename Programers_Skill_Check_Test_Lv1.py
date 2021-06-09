def solution(nums) :
    answer = 0
    max = len(nums)
    for i in range(max) :
        for j in range(i+1, max) :
            for k in range(j+1, max) :
                sum = nums[i] + nums[j] + nums[k]
                for l in range(2, sum) :
                    if sum % l == 0 :
                        # print(sum, l)
                        prime_number = False
                        break
                    else:
                        prime_number = True
                if prime_number :
                    answer+=1
    return answer

nums = [1, 2, 7,6, 4]

print(solution(nums))

