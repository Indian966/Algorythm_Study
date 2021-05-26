N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# N, C = 5,3
# arr = [1,2,8,4,9]
arr.sort()
low = 1
high = arr[-1] - arr[0]
result = 0
while (low <= high):
    mid = (low + high) // 2
    old = arr[0]
    count = 1

    for i in range(1, N):
        if arr[i] >= old + mid:
            count += 1
            old = arr[i]
    if count >= C:
        low = mid + 1
        result = mid
    else:
        high = mid - 1
print(result)