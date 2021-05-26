import sys

N = int(input())
N_arr = set(list(map(int, sys.stdin.readline().split())))
M = int(input())
M_arr = set(list(map(int, sys.stdin.readline().split())))

# N = 5
# N_arr = [6, 3, 2, 10, -10]
# M = 8
# M_arr = [10, 9, -5, 2, 3, 4, 5, -10]
# answer = [] #0 for _ in range(N)

# def binary_search(value):
#     N_arr.sort()
#     low = 0
#     high = len(N_arr) - 1
#     while (low <= high):
#         mid = (low + high) // 2
#         if N_arr[mid] == value :
#             return 1
#             break
#         elif N_arr[mid] > value:
#             high = mid - 1
#         elif N_arr[mid] < value:
#             low = mid + 1
#     return 0
#
# for i in M_arr :
#     # answer.append(binary_search(N_arr,i))
#     print(binary_search(i),end=' ')
# # print(answer)

for i in M_arr :
    if i in N_arr :
        print(1, end=' ')
    else:
        print(0, end=' ')