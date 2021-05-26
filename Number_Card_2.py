import sys
import time
from collections import Counter

# N = int(input())
# N_arr = list(map(int, sys.stdin.readline().split()))
# M = int(input())
# M_arr = list(map(int, sys.stdin.readline().split()))

start = time.time()

N = 10
N_arr = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
M = 8
M_arr = [10, 9, -5, 2, 3, 4, 5, -10]

C = Counter(N_arr)
print(' '.join(f'{C[m]}' if m in C else '0' for m in M_arr))
print("time :", time.time() - start)
