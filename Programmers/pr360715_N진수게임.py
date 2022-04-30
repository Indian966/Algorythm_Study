# 자신이 말해야 하는 숫자를 스마트폰에 미리 출력해주는 프로그램을 만들려고 한다.
# 튜브의 프로그램을 구현하라.
# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p 가 주어진다.
# n	    t	m	p	result
# 2	    4	2	1	"0111"
# 16	16	2	1	"02468ACE11111111"
# 16	16	2	2	"13579BDF01234567"

n , t, m, p = 2, 4, 2, 1

def solution(n, t, m, p):
    answer = ''
    def converter (n, q) :
        rev_base = ''

        while n > 0:
            n, mod = divmod(n, q)
            rev_base += str(mod)

        return rev_base[::-1]
    cnt = 0
    numb = 0
    result = []
    flag = 0
    while cnt<=t :
        arr = converter(numb, n)

        for i in range(len(arr)):
            if flag == p:
                result.append(arr[i])
                cnt+=1
            if flag == m:
                flag = 0
            flag += 1
        numb+=1

    return result

print(solution(n , t, m, p))
