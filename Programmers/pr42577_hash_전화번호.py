# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이
# solution 함수의 매개변수로 주어질 때,
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를
# 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

phone_book = ["1", "01", '013']
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1) :
        if phone_book[i] == (phone_book[i+1])[:len(phone_book[i])] :
            return False
    return answer

print(solution(phone_book))

# def solution(p):
#
#     p.sort()
#     for i in range(len(p)-1):
#         if p[i] == (p[i+1])[:len(p[i])] :
#             return False
#
#     return True