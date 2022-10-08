"""
    사내의 팀원들 전체를 대상으로 랜덤한 조를 구성하려고 합니다. 한 조는 최소 5명, 최대 7명으로
    구성하고, 조의 개수는 최소화해야 합니다
    핵심은 팀원의 숫자를 최대한 7명 단위로 쪼개면서
    나머지 인원들을 6 내지 5명으로 구성하는 것
"""



def mix_members (members) :
    answer = []

    numb = members
    mok_7, r = divmod(numb, 7)
    mok_6 = 0
    mok_5 = 0

    # 70명 이하라면 그냥


    # 총원을 7로 나눈 나머지가 6의 배수인지, 5의 배수인지 검사 후
    # 맞다면
    while True:
        # 6의 배수가 아니면서 5의 배수일 때
        if (r % 6) > 0 and not (r % 6) % 5:
            q_6 = r // 6
            q_5 = r % 6 // 5
            break
        # 6의 배수일 때
        elif not r % 6:
            q_6 = r // 6
            break
        elif not r % 5:
            q_5 = r // 5
            break

        mok_7 -= 1
        r += 7
    print(mok_7, mok_6, mok_5)

    return answer

# m = [5, 7, 10, 22]
# # 이름 대신 숫자
# members = [i for i in range(m)]

# print(mix_members(members))


# result 18 1 0
print(mix_members(132))