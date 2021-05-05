

graph = {
    1:(0, 0), 2:(0, 1), 3:(0, 2),
    4:(1, 0), 5:(1, 1), 6:(1, 2),
    7:(2, 0), 8:(2, 1), 9:(2, 2),
    '*':(3, 0), 0:(3, 1), '#':(3, 2)}


def solution(numbers, hand):
    answer = ''
    left_pointer = '*'
    right_pointer = '#'
    left, right = set([1, 4, 7]), set([3, 6, 9])

    for numb in numbers:
        if numb in left:
            answer += "L"
            left_pointer = numb
        elif numb in right:
            answer += "R"
            right_pointer = numb
        else:
            answer += distance_calc(numb, left_pointer,right_pointer, hand)
            if answer[-1] == 'L':
                left_pointer = numb
            else:
                right_pointer = numb

    return answer

def distance_calc(num, now_l, now_r, handed):
    X, Y = 0, 1
    dist_l = abs(graph[now_l][X] - graph[num][X]) + abs(graph[now_l][Y] - graph[num][Y])
    dist_r = abs(graph[now_r][X] - graph[num][X]) + abs(graph[now_r][Y] - graph[num][Y])
    if dist_l == dist_r:
        return 'R' if handed == 'right' else 'L'
    return 'R' if dist_l > dist_r else 'L'


numbers = list(map(int,input()))
print(numbers)
hand = str(input())
left_pointer = '*'
right_pointer = '#'

print(solution(numbers, hand))

# [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# 13458214595
# ['1','3','4']
# [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# 70828315762
