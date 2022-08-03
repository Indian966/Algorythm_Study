def check(s):
    stack = []
    open = '([{'
    close = ')]}'
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
        else :
            stack.pop()

    return len(stack) == 0

print(check('()'))