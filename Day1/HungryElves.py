calsInfo = open("Day1/cals.txt").read().splitlines()

currentTotal = 0
calList=[]
for line in calsInfo:
    if line == '':
        calList.append(currentTotal)
        currentTotal = 0
    else:
        currentTotal += int(line)


calList.sort(reverse=True)

print(calList[0] + calList[1] + calList[2])