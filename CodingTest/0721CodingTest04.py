
foods = [1,2,3,0,3]

def solution(foods):
    if len(foods) >= 3 :
        count = 0
        for i in range(1, len(foods) - 1):
            for j in range(i + 1, len(foods)):
                A = sum(foods[:i])
                B = sum(foods[i:j])
                C = sum(foods[j:])
                if A == B and B == C:
                    count += 1
        answer = count
    else:
        answer = 0

    return answer

print(solution(foods))