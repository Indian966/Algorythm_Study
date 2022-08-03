
arr = [4,4,4,3,3,]

def solution(arr):
    answer = []
    before = -1

    # item과  before가 같지 않다면 answer에 담아서 return
    for item in arr :
        if before != item :
            answer.append(item)
            before = item
    return answer

print(solution(arr))
