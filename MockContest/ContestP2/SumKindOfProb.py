lines = int(input())
allVals = []
for i in range(1,lines+1):
    vals = [int(x) for x in input().split()]
    sumList = []
    sumList.append(vals[0])
    # summation formula
    sumList.append( int( ( (vals[1]) * ( (vals[1])+1) ) / 2 ) ) # all positive 
    sumList.append( int( (vals[1]) * (vals[1]) ) ) # odd
    sumList.append( int( (vals[1]) * ( (vals[1]) + 1 ) ) ) # even
    allVals.append(sumList)


for i in range(len(allVals)):
    print(allVals[i][0],allVals[i][1],allVals[i][2], allVals[i][3])
