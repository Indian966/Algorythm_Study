T = int(input())
for i in range(1, T+1) :
    N = int(input())
    arr = [input() for _ in range(N)]
    arr = list(set(arr))
    sorted_list = sorted(arr, key=lambda x: (len(x), x))
    print(f"#{i}")
    for j in sorted_list :
        print(j)
