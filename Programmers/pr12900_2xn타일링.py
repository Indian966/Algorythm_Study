# 간단한 피보나치 수열이었다
n = 3
def solution(n):
    def fib(n):
        _curr, _next = 1, 2
        for _ in range(n):
            _curr, _next = _next, _curr + _next
        return _curr


    return fib(n-1) % 1000000007

solution(n)