import sys

T = int(input())
# N, M = map(int, sys.stdin.readline().split())
array=[0 for _ in range(T)]
for i in range(T):
    array[i]=list(map(int, list(sys.stdin.readline().split())))
schedule = []
def selctionSort(a) :
    n = len(a)
    for i in range(n) :
        small = i
        for j in range(i+1, n) :
            if a[j][0] < a[small][0] :
                small = j
        a[i], a[small] = a[small], a[i]
    return  a
selctionSort(array)

print()

