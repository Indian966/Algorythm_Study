T = int(input())
for i in range(1, T+1) :
    compare = list(map(int, input().strip()))

    init = 0
    count = 0
    for j in compare :
        if init != j:
            count += 1
            init = j

    print("#{} {}".format(i, count))