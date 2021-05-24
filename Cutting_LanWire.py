import sys

# K, N = map(int, sys.stdin.read().split())
#
# arr = [int(input()) for _ in range(K)]
# print(arr)

K, N = 4, 11
arr = [802, 743, 457, 539]
arr.sort()
print(sum(arr))
wire = sum(arr) // N
print(wire)
flag = True

S = [5, 8, 1, 3, 7, 2, 6, 9]


def binary_search(arr, value):
    low = 0
    high = len(arr) - 1
    while (low <= high):
        mid = (low + high) // 2
        if arr[mid] > value:
            high = mid - 1
        elif arr[mid] < value:
            low = mid + 1
        else:
            return mid

print(binary_search(S, 9))