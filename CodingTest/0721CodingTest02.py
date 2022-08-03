

s = 'zxzxz'
def solution(s):
    answer = 0
    arr = set()
    for i in range(len(s)) :
        for j in range(i, len(s)) :
            temp = s[i:j+1]
            arr.add(temp)

    # 집합의 원소 탐방
    for i in arr :
        # 원소의 길이가 2이상일때
        if len(i) >= 2 :
            # 문자열에 중복되는 알파벳이 없다면
            if len(i) == len(set(i)) :
                answer+=1
        else:
            answer+=1

    return answer

print(solution(s))