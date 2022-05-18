# citations	        return
# [3, 0, 6, 1, 5]	3


citations = [10, 10, 10, 10, 10]

def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for i in range(len(citations)) :
        if i >= citations[i] :
            answer=i
            break
        else:
            answer = i+1

    return answer

print(solution(citations))

def another_solution(citiations) :

    citiations.sort(reverse=True)
    answer = max(map(min, enumerate(citiations, start=1)))

    return answer


print(another_solution(citations))