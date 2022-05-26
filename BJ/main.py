T = int(input())
for i in range(1, T+1) :
    total_clothes = int(input())
    total_clothes += 1
    total_price = 0
    arr = []
    clothes = input()
    arr = clothes.split()
    arr.sort(reverse=True)
    arr.insert(0, "0")
    for n in range(total_clothes):
        if n % 3:
            total_price = total_price + int(arr[n])
    print("#{} {}".format(i, total_price))