T = int(input())
global count
count = 0


def Nqueen(arr, n):
    if len(arr) == n  :
        count += 1
        return 0

for test_case in range(1, T + 1):
    N = int(input())
    Nqueen([test_case], N)

