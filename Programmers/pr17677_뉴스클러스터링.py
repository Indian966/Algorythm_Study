# 입력으로 들어온 두 문자열의 자카드 유사도를 출력한다.
# 유사도 값은 0에서 1 사이의 실수이므로,
# 이를 다루기 쉽도록 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력한다.

# str1	    str2	    answer
# FRANCE	french	    16384
# handshake	shake hands	65536
# aa1+aa2	AAAA12	    43690
# E=M*C^2	e=m*c^2	    65536

str1 = ['FRANCE', 'handshake', 'aa1+aa2', 'E=M*C^2']
str2 = ['french', 'shake hands', 'AAAA12', 'e=m*c^2']
def solution(str1, str2):
    answer = 0

    def divider (word) :
        result = []
        for i in range(len(word)) :
            if i == len(word)-1 : break
            if word[i].isalpha() == False or word[i+1].isalpha() == False :
                continue
            else:
                result.append((word[i] + word[i+1]).upper())
        return result

    def intersection(a, b) :
        common = []
        for i in b :
            if i in a :
                a.remove(i)
                common.append(i)
        return len(common)

    def union (a, b) :
        a1 = a.copy()
        a2 = a.copy()
        for i in b :
            if i not in a1 :
                a2.append(i)
            else :
                a1.remove(i)
        return len(a2)

    a = divider(str1)
    b = divider(str2)

    return (65536 if union(a,b) == 0 else int(intersection(a,b) / union(a,b) * 65536))


for i,j in zip(str1, str2) :
    print(solution(i,j))