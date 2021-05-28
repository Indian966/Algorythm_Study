# N, H = map(int, input().split())
# arr = [int(input()) for _ in range(N)]

N = 14
H = 5
arr = [1,3,4,2,2,4,3,4,3,3,3,2,3,3]

l_arr = []
h_arr = []

for i in range(len(arr)) :
    if i % 2 : h_arr.append(arr[i])
    else: l_arr.append(arr[i])

l_arr.sort()
h_arr.sort()

min_len = N
distroy_count = 0

def binary_search(arr, value, arr_length):
    low = 0
    high = arr_length
    while (low <= high):
        mid = (low + high) // 2

        if arr[mid] < value :
            low = mid + 1
        else:
            high = mid - 1
    return low

for i in range(1,H+1) :
    down = len(l_arr) - binary_search(l_arr, i - 0.5, len(l_arr)-1)
    up = len(h_arr) - binary_search(h_arr, H - i + 0.5, len(h_arr) - 1)

    if min_len > (down + up) :
        distroy_count = 1
        min_len = down + up
    elif min_len == (down + up) :
        distroy_count += 1

print(min_len, distroy_count)