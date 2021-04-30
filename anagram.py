first = sorted(list(input()))
second = sorted(list(input()))
count=0
tempA = list ()

for i in first :
    tempA.append(i)
    if i  in second:
        tempA.remove(i)
        second.remove(i)
count = len(second) + len(tempA)
print(count)
#aabbcc
#xxyybb