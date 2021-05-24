import sys

K, N = map(int, sys.stdin.read().split())
arr = [int(input()) for _ in range(K)]
arr.sort(reverse=True)

def binary_search(arr, N):
    low = 0
    high = arr[0]

    while (low <= high):
        sum = 0
        mid = (high+low) // 2
        for i in arr :
            sum += i // mid
        if sum < N or arr[-1] < mid:
            high = mid
        elif sum > N :
            low = mid
        else :
            return mid
            break

print(binary_search(arr, N))