T = int(input())
for i in range(T):
    # sticker_1 = [[50, 10, 100, 20, 40], [30, 50, 70, 10, 60]]
    # sticker_2 = [[10, 30, 10, 50, 100, 20, 40] ,[20, 40, 30, 50, 60, 20, 80]]
    sticker = []
    n = int(input())
    for _ in range(2):
        sticker.append(list(map(int, input().split())))
    sticker[0][1] += sticker[1][0]
    sticker[1][1] += sticker[0][0]
    for j in range(2,n) :
        sticker[0][j] += max(sticker[1][j - 1], sticker[1][j - 2])
        sticker[1][j] += max(sticker[0][j - 1], sticker[0][j - 2])
    print(max(sticker[0][n - 1], sticker[1][n - 1]))
