# 자연수 n이 매개변수로 주어질 때,
# n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.
# 10진법	124 나라	10진법	124 나라
# 1	    1	    6	    14
# 2	    2	    7	    21
# 3	    4	    8	    22
# 4	    11	    9	    24
# 5	    12	    10	    41

def solution(n):
    answer = ''

    while n>0 :
        m, mod = divmod(n,3)
        if mod == 0:
            answer += str(4)
            n = n//3 -1
        else:
            answer += str(mod)
            n = n//3
    return answer[::-1]

print(solution(10))


