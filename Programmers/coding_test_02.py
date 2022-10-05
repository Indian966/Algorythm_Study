rooms =["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"]
target = 403
def solution(rooms, target):
    answer = []

    workers = dict()
    for line in rooms :
        temp = line.split(']')
        emp = temp[1].split(',')
        for e in emp :
            workers[e] = []

    for line in rooms :
        temp = line.split(']')
        room = temp[0][1:]
        emp = temp[1].split(',')
        for e in emp :
            workers[e].append(room)
    print(workers)
    name = list(workers.keys())
    dist=dict()
    for i in range(len(name)) :
        # print(name[i])
        room_list = workers[name[i]]
        # print(room_list)
        if str(target) in room_list :
            dist[name[i]] = 0
        else :
            temp = []
            for r in room_list :
                temp.append(abs(int(r)-target))
            dist[name[i]] = min(temp)
            # print(dist)
    name.sort()
    for n in name :
        # print(len(workers[n]))
        if str(target) not in workers[n] and dist[n]:
            answer.append(n)
            answer.sort(key=lambda x: dist[x])
            answer.sort(key=lambda x:len(workers[x]))

    return answer

print(solution(rooms,target))
