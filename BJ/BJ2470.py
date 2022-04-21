import sys

# N = int(input())
# arr = list(map(int, sys.stdin.readline().split()))

N = 5
arr = [-2, 4, -99, -1, 98]

def binary_search():
    arr.sort()
    low = 0
    high = N-1
    answer = arr[low] + arr[high]
    answer_low = low
    answer_high = high
    while (low < high):
        mid = arr[low] + arr[high]
        if abs(mid) < abs(answer):
            answer = mid
            answer_low = low
            answer_high = high
            if mid == 0 :
                break
        if mid < 0 :
            low += 1
        else:
            high-=1
    print(arr[answer_low],arr[answer_high])

binary_search()
