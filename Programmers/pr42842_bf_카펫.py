# brown	yellow	return
# 10	2	    [4, 3]
# 8	    1	    [3, 3]
# 24	24	    [8, 6]


brown = 10
yellow = 2

def solution(brown, yellow):
    answer = []

    for x in range(1, brown//2+1) :
        y = (brown-4)//2 - x
        expect = x * y
        if x>=y and expect == yellow :
            answer = [x+2,y+2]
            break
    return answer

print(solution(brown,yellow))