T = int(input())

array=[0 for _ in range(1,T+1)]
global group_count
group_count = 0
group_size = []

def search(row, column)  :
    if array[row][column+1] or array[row+1][column] or array[row][column-1] or array[row-1][column] :
        return False
    return True

def dfs(number) :
    for i in range(number) :
        if array[number][i] :
            if search(number, i) : continue

        else: continue
        if search(number, i): continue
        dfs(number+1)
        group_count += 1


for i in range(T):
    array[i]=list(map(int, list(str(input()))))
print(group_size.__sizeof__())







# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000