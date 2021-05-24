arr = {
    0 : "무지", 1 : "콘", 2 : "어피치",
    3 : "제이지", 4 : "프로도", 5 : "네오",
    6 : "튜브", 7 : "라이언"
}

def solution(n, k, cmd):
    pre_col = ["무지", "콘", "어피치", "제이지", "프로도", "네오", "튜브", "라이언"]
    post_col = ["무지", "콘", "어피치", "제이지", "프로도", "네오", "튜브", "라이언"]
    answer = ''
    trash_can = []
    for co in cmd :
        s_com = list(co.split())
        if "U" in s_com :
            k -= int(s_com[-1])
            if k < 0 :
                k = 0
            print(s_com, k)
        elif "D" in s_com :
            k += int(s_com[-1])
            if k >= len(pre_col) :
                k = len(pre_col) - 1
            print(s_com, k)
        elif "C" in s_com and len(pre_col)>0 and k < len(pre_col):
            trash_can.append(k)
            trash_can.append(pre_col[k])
            del pre_col[k]
            if k > len(pre_col) :
                k-=1
            elif k == len(pre_col):
                k = len(pre_col)-1
            print(s_com, k, pre_col, trash_can)
        elif "Z" in s_com and len(trash_can)>0:
            if trash_can[-2] <= k :
                k+=1
            pre_col.insert(trash_can[-2], trash_can[-1])
            del trash_can[-2:]
            print(s_com, k, pre_col, trash_can)

    for j in post_col :
        if j in trash_can :
            answer += "X"
        else: answer += "O"

    print(pre_col)
    print(answer)
    return answer


arr1 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
arr2 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
arr3 = ["D 6", "C", "C", "U 5", "D 10"]
solution(8, 2, arr2)
