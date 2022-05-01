# 예를 들어 begin이 "hit", target가 "cog",
# words가 ["hot","dot","dog","lot","log","cog"]라면
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.
#
# 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때,
# 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지
# return 하도록 solution 함수를 작성해주세요.
from collections import deque

begin = 'hit'
target = 'cog'
words = ["hot","dot","dog","lot","log","cog"]


def solution(begin, target, words):
    size = len(begin)
    visited = [0 for _ in range(size)]
    que = deque()
    arr = []
    for index in range(size) :
        arr.append(begin[index])
    if target not in words :
        return 0

    def check_dif (word1, word2) :
        count = 0
        for i in range(len(word1)) :
            if word1[i] == word2[i] :
                count += 1
        if count == len(word1)-1 :
            return True
        else:
            return False
    for wd in words :
        if check_dif(begin, wd) :
            que.append([wd, 1])

    while que :
        word, cnt = que.popleft()
        if word == target :
            return cnt
        for wd in words :
            if check_dif(word, wd) :
                if wd == target :
                    return cnt+1
                que.append([wd, cnt+1])
    answer = 0
    return answer

print(solution(begin,target,words))