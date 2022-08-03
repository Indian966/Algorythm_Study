s1 = "[]([[]){}" # 3
s2 = "{([()]))}" # 4
s3 = "(()()()" # 7

def solution(s) :
    answer = 0
    need = ''

    if s.count('(') > s.count(')') :
        need = ')'
    elif s.count('(') < s.count(')') :
        need = '('
    elif s.count('[') > s.count(']'):
        need = ']'
    elif s.count('[') < s.count(']'):
        need = '['
    elif s.count('{') > s.count('}'):
        need = '}'
    elif s.count('{') < s.count('}'):
        need = '{'

    def check(s):
        stack = []
        open = '([{'
        for c in s:
            if c in open:
                stack.append(c)
            elif c == ')' and stack and stack[-1] != '(':
                return False
            elif c == ']' and stack and stack[-1] != '[':
                return False
            elif c == '}' and stack and stack[-1] != '{':
                return False
            elif not stack:
                return False
            else:
                stack.pop()
        return len(stack) == 0

    for i in range(len(s)+1) :
        array = s[:i] + need + s[i:]
        if check(array) :
            answer+=1

    return answer

print(solution(s2))
