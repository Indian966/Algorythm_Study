record = ["Enter uid1234 Muzi",
          "Enter uid4567 Prodo",
          "Leave uid1234",
          "Enter uid1234 Prodo",
          "Change uid4567 Ryan"]

# 채팅방에 들어올때, 혹은 닉네임 바꿨다고 Change할때 닉을 바꿀 수 있음
# ["Prodo님이 들어왔습니다.",
# "Ryan님이 들어왔습니다.",
# "Prodo님이 나갔습니다.",
# "Prodo님이 들어왔습니다."]

def solution(record):
    answer = []
    uid = dict()
    for line in record :
        log = line.split(' ')
        if log[0] == 'Enter' or log[0] == 'Change' :
            uid[log[1]] = log[2]
    for line in record :
        log = line.split(' ')
        if log[0] == 'Enter' :
            string = uid[log[1]] + "님이 들어왔습니다."
            answer.append(string)
        elif log[0] == 'Leave' :
            string = uid[log[1]] + "님이 나갔습니다."
            answer.append(string)

    return answer

print(solution(record))