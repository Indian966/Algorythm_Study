# 열쇠를 나타내는 2차원 배열 key와
# 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때,
# 열쇠로 자물쇠를 열수 있으면 true를,
# 열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.


key = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
lock = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]


# 회전
def rotate(k):
    n = len(k)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - i - 1] = k[i][j]
    return result


# 확인
def check(l):
    n = len(l) // 3
    # new_lock의 중간 부분이 모두 1인지 확인
    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if l[i][j] != 1:
                return False
    return True


def solution(key, lock):
    answer = False
    n = len(lock)
    m = len(key)

    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 세배 확장된 lock을 만든다.
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 매 회전
    for r in range(4):
        key = rotate(key)
        # 매 이동
        for x in range(1, n * 2):
            for y in range(1, n * 2):

                # 열쇠를 넣어준다.
                for i in range(m):
                    for j in range(m):
                        # lock에 key를 더해줌
                        new_lock[x + i][y + j] += key[i][j]

                # 해당 열쇠가 맞는지 검사
                if check(new_lock) == True:
                    return True

                # 맞지 않는다면 되돌린다(열쇠를 뺀다)
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False

print(solution(key, lock))