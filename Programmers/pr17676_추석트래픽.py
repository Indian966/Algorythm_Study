# 9월 15일 로그 데이터를 분석한 후 초당 최대 처리량을 계산해보기로 했다.

line = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

def solution(lines):
    answer = set([0])
    time_line = []
    for arr in lines :
        temp = arr.split()
        time = temp[1].split(':')

        end_time = (int(time[0]) * 3600) + (int(time[1]) * 60 ) + float(time[2])
        cost = temp[2]
        start_time = end_time - float(cost[:-1]) + float(0.001)
        time_line.append([start_time, end_time])

    for time in time_line :
        cur = 0
        for i in time_line :
            if i[1] >= time[1] and i[0] < time[1]+1 :
                cur+=1
        answer.add(cur)

    return max(answer)



def anoter_solution(lines):

    #get input
    S , E= [], []
    totalLines = 0
    for line in lines:
        totalLines += 1
        type(line)
        (d,s,t) = line.split(" ")

       ##time to float
        t = float(t[0:-1])
        (hh, mm, ss) = s.split(":")
        seconds = float(hh) * 3600 + float(mm) * 60 + float(ss)

        E.append(seconds + 1)
        S.append(seconds - t + 0.001)

    #count the maxTraffic
    S.sort()
    print(E)
    print(S)

    curTraffic = 0
    maxTraffic = 0
    countE = 0
    countS = 0
    while((countE < totalLines) & (countS < totalLines)):
        if(S[countS] < E[countE]):
            curTraffic += 1
            maxTraffic = max(maxTraffic, curTraffic)
            countS += 1
        else: ## it means that a line is over.
            curTraffic -= 1
            countE += 1

    return maxTraffic

print(anoter_solution(line))