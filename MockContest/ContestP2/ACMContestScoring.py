# logs = [x for x in input().split()]
totalLogs = []
# for i in sys.stdin:
    # logs = [x for x in input().split()]
    # totalLogs.append(logs)
while True:
    logs = [x for x in input().split()]
    if(logs[0] == "-1"):
        break
    totalLogs.append(logs)

right = []
time = 0
for i in range(len(totalLogs)):
    if(totalLogs[i][2] == "right"):
        if totalLogs[i][1] in right: # case to dismiss muliple correct submssions
            continue
        time += int(totalLogs[i][0])
        right.append(totalLogs[i][1])
for i in range(len(totalLogs)):
    if(totalLogs[i][2] == "wrong"):
        if totalLogs[i][1] in right:
            time += 20
print(len(right), " " ,time)