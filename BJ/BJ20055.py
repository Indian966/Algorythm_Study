import sys

# N = int(input())
# K = int(input())
# durability = list(map(int, sys.stdin.readline().split()))

N = 3
K = 2
durability = [1, 2, 1, 2, 1, 2]

belt = []
for _ in range(N*2) :
    belt.append(0)
count = 0
while count >= K :
    print(belt)
    print(durability)
    level = 1
    for i in range(level) :
        print(belt)
        print(durability)
        if belt[i] == 0 and durability[i] >= 1:
            belt[i] = 1
            durability[i] -= 1
            if i >= 1 :
                belt[i-1] = 0

        elif durability[i] == 0 :
            count += 1

    level+=1
print(count)