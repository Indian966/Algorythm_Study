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
    def diff (word1, word2) :
        a = []
        for i in word1 :
            if i.isalpha() :
                a.append(i)
        for j in range(len(a)) :


    diff(str1[3], str2[0])

    return answer

print(solution(str1,str2))