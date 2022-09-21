# n	words	        result
# 3	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	[3,3]
# 5	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]	[0,0]
# 2	["hello", "one", "even", "never", "now", "world", "draw"]	[1,3]


def solution(n, words):
    answer = []
    circle = 0
    person = 0

    before = []
    for i in range(len(words)) :
        if i == 0 :
            before.append(words[i])
        elif i > 0 and len(answer) == False :
            cur = words[i]
            if before[-1][-1] != cur[0] or cur in before:

                m, r = divmod(i+1, n)
                if r == 0 :
                    circle=m
                    person=n
                else :
                    circle=m+1
                    person=r

                break
            before.append(cur)

    answer.append(person)
    answer.append(circle)
    return answer

# [3,3]
n1 = 3
words1 = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

# [0,0]
n2 = 5
words2 = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]

# [1,3]
n3 = 2
words3 = ["hello", "one", "even", "never", "now", "world", "draw"]


print(solution(n1, words1))
print(solution(n2, words2))
print(solution(n3, words3))