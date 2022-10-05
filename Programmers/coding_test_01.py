# 상태	미세먼지 농도
# 좋음	30 이하
# 보통	31 ~ 80
# 나쁨	81 ~ 150
# 매우나쁨	151 이상
# 상태	초미세먼지 농도
# 좋음	15 이하
# 보통	16 ~ 35
# 나쁨	36 ~ 75
# 매우나쁨	76 이상

atmos = [[140, 90], [177, 75], [95, 45], [71, 31], [150, 30], [80, 35], [72, 33], [166, 81], [151, 75]]
# return 3

def solution (atmos) :
    answer = 0
    mask = 0
    for i, j in atmos :

        if i > 150 and j > 75 :
            print(i,j)
            answer+=1
            mask = 0
        elif i>80 or j>35 :
            mask+=1
            if mask == 3:
                print(i,j)
                answer += 1
                mask = 0
        elif i<=80 and j<=35 :
            if mask>0 :
                mask+=1
            if mask == 3:
                print(i,j)
                answer+=1
                mask = 0
    if mask>0 :
        answer+=1
    return answer



print(solution(atmos))