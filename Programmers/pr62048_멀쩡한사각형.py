import math
w=3
h=5

def solution(w,h):
    answer = w * h
    box = 0
    def line(x) :
        y = (h/w) * x
        return y
    for x in range(1, w+1) :
        big = math.ceil(line(x))
        small = math.floor(line(x-1))
        box += big-small

    return answer - box

def another_solution(w, h) :
    return w * h - (w + h - math.gcd(w,h))


print(another_solution(w,h))