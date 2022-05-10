# 특정 튜플을 표현하는 집합이 담긴 문자열 s가 매개변수로 주어질 때,
# s가 표현하는 튜플을 배열에 담아 return 하도록 solution 함수를 완성해주세요.

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"

def solution(s):
    answer = []
    s = s[1:-1]
    # print(list(s.split()))
    number = set()
    for i in s :
        if i.isalnum() :
            number.add(int(i))
    # print(number)
    answer = list(number)
    return answer

print(solution(s))
