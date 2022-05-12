# 만들고자 하는 이름 name이 매개변수로 주어질 때,
# 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.


name = 'JAZ'

def solution(name):
    answer = 0
    start = 0
    count = 0
    dist = []
    for i in range(len(name)) :
        if name[i] != 'A' :
            # print(ord('A'))
            # print(ord(name[i]))
            right = ord(name[i]) - 65
            left = 90 - ord(name[i]) + 1
            if left < right :
                dist.append(left)
            else:
                dist.append(right)
        else:
            dist.append(0)





    return answer

print(solution(name))
