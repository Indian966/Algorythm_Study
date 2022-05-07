# s	        result
# baabaa	1
# cdcd	    0
from collections import deque
s = 'bbabba'
def solution(s):
    stack = []
    for c in s :
        if (not stack) :
            stack.append(c)
        else:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
    if stack :
        return 0

    return 1

print(solution(s))