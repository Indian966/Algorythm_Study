# 압축할 문자열 s가 매개변수로 주어질 때,
# 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중
# 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.

s = "ababcdcdababcdcd"

def solution(s):
    answer = len(s)
    length = len(s)

    for i in range(1,length//2+1) :
        compressed = ''
        prev = s[0:i]
        count = 1
        for j in range(i, length, i) :
            if prev == s[j:i+j] :
                count += 1
            else:
                if count >= 2 :
                    compressed += str(count) + prev
                else:
                    compressed += prev
                prev = s[j:j+i]
                count = 1
        if count >= 2 :
            compressed += str(count) + prev
        else:
            compressed += prev
        answer = min(answer, len(compressed))

    return answer

print(solution(s))
min(compress(text, tok_len) for tok_len in list(range(1, int(len(text) / 2) + 1)) + [len(text)])

def another_solution (s) :
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                if count >= 2:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                prev = s[j:j + step]
                count = 1
        if count >= 2:
            compressed += str(count) + prev
        else:
            compressed += prev
        answer = min(answer, len(compressed))
    return answer