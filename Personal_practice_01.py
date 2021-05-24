import sys

arr = {
    "zero" : 0, "one" : 1, "two" : 2,
    "three" : 3, "four" : 4, "five" : 5,
    "six" : 6, "seven" : 7, "eight" : 8,
    "nine" : 9
}

def solution(s):
    answer = ""
    list(s)
    numbers = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    temp = ""
    for i in s :
        if i in numbers :
            answer += i
        else :
            temp += i
            if temp in arr :
                answer += str(arr[temp])
                temp = ""

    return int(answer)
#one4seveneight
# N= map(str, sys.stdin.readline().split()
N = sys.stdin.readline()
print(solution(N))
