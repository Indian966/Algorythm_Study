"""
    사내의 팀원들 전체를 대상으로 랜덤한 조를 구성하려고 합니다. 한 조는 최소 5명, 최대 7명으로
    구성하고, 조의 개수는 최소화해야 합니다
    핵심은 팀원의 숫자를 최대한 7명 단위로 쪼개면서
    나머지 인원들을 6 내지 5명으로 구성하는 것
"""
from collections import defaultdict
import random

def mix_members (mem_numb) :
    answer = []
    member_list = [i for i in range(mem_numb)]
    member_dict = defaultdict(list)

    div_seven = mem_numb // 7

    # 70명 미만일때는 5명으로 우선 나누고 나머지를 각 조에 뿌리는게 편함
    if div_seven < 10 :
        for i in range(1, 11) :
            for _ in range(5) :
                out_mem = random.choice(member_list)
                member_list.remove(out_mem)
                member_dict[f'{i}조'].append(out_mem)

            # 나머지 멤버 넣어주기
            group_cnt = 1
            while member_list :
                if len(member_dict[f'{group_cnt}조']) < 7:
                    out_mem = random.choice(member_list)
                    member_list.remove(out_mem)
                    member_dict[f'{group_cnt}조'].append(out_mem)
                else:
                    group_cnt += 1
    else :
        numb = mem_numb
        mok_7, r = divmod(numb, 7)
        mok_6 = 0
        mok_5 = 0

        # 70명 이하라면 그냥

        # 총원을 7로 나눈 나머지가 6의 배수인지, 5의 배수인지 검사 후
        # 맞다면
        while True :
            # 6의 배수가 아니면서 5의 배수일 때
            if (r % 6) > 0 and not (r % 6) % 5 :
                q_6 = r // 6
                q_5 = r % 6 // 5
                break
            # 6의 배수일 때
            elif not r % 6 :
                q_6 = r // 6
                break
            elif not r % 5 :
                q_5 = r // 5
                break

            mok_7 -= 1
            r += 7

        # 7명 조의 숫자만큼 딕셔너리에 추가
        group_cnt = 1
        for _ in range(1, mok_7 + 1) :
            for _ in range(7) :
                out_mem = random.choice(member_list)
                member_list.remove(out_mem)
                member_dict[f'{group_cnt}조'].append(out_mem)
            group_cnt += 1

        # 6명 조의 숫자만큼 딕셔너리에 추가
        for _ in range(1, mok_6 + 1) :
            for _ in range(6) :
                out_mem = random.choice(member_list)
                member_list.remove(out_mem)
                member_dict[f'{group_cnt}조'].append(out_mem)
            group_cnt += 1

        # 5명 조의 숫자만큼 딕셔너리에 추가
        for _ in range(1, mok_5 + 1) :
            for _ in range(5) :
                out_mem = random.choice(member_list)
                member_list.remove(out_mem)
                member_dict[f'{group_cnt}조'].append(out_mem)
            group_cnt += 1

    return member_dict


# result 18 1 0
print(mix_members(132))