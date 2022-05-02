# 각 도시의 트럭을 최적으로 운행했을 때,
# 새로운 도시를 건설하기 위해 금 a kg과 은 b kg을 전달할 수 있는 가장 빠른 시간을 구해
# return 하도록 solution 함수를 완성해주세요.

# a	    b	g	        s	        w	        t	    result
# 10	10	[100]	    [100]	    [7]	        [10]    50
# 90	500	[70,70,0]	[0,0,500]	[100,100,2]	[4,8,1]	499

a=10 # 필요한 금
b=10 # 필요한 은
g = [100] # 가지고 있는 금
s = [100] # 가지고 있는 은
w = [7] # 한번에 운반 가능한 무게
t = [10] # 이동 시간

def solution(a, b, g, s, w, t):
    answer = int(10 ** 16)
    left, right = 0, int(10 ** 16)

    while left <= right :
        mid = (left + right) // 2
        moved_gold = 0
        moved_silver = 0
        total = 0
        for i in range(len(g)) :
            movment_count = mid // (t[i] * 2)

            # 맨 마지막에 편도로 이동 가능한 경우
            if mid % (t[i] * 2) >= t[i] :
                movment_count+=1
            # 제한시간 동안 금, 은 운반
            city_gold = w[i] * movment_count if w[i] * movment_count <= g[i] else g[i]
            city_silver = w[i] * movment_count if w[i] * movment_count <= s[i] else s[i]
            moved_gold += city_gold
            moved_silver += city_silver
            total+= w[i] * movment_count if s[i] + g[i] >= w[i] * movment_count else s[i] + g[i]

        if moved_gold >= a and moved_silver >= b and total >= a + b :
            right = mid -1
            answer = min(answer, mid)
        else :
            left = mid + 1

    return answer

print(solution(a,b,g,s,w,t))