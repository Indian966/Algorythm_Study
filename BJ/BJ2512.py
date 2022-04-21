import sys
# N = int(input())
# arr = list(map(int, sys.stdin.readline().split()))
# M = int(input())

N = 4
arr = [120, 110, 140, 150]
M = 485

def binary_search(arr, N):
    arr.sort()
    low = 0
    high = max(arr)

    while (low <= high):
        sum = 0
        mid = (low + high) // 2
        for i in arr :
            sum += min(mid, i)

        if sum > M:
            high = mid - 1
        else:
            low = mid + 1
    print(high)

binary_search(arr,N)