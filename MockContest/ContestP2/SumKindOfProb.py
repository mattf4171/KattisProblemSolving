import numpy as np

lines = int(input())
allVals = []
tempVals = []
cumsum = []
# predefined 
cumsum = np.cumsum(np.arange(0,10000,1)) 
oddSum = np.cumsum(np.arange(1,10000,2)) 
evenSum = np.cumsum(np.arange(2,10000,2)) 

for i in range(lines):
    values = [int(x) for x in input().split() ]
    sumList = []
    sumList.append(values[0])
    sumList.append(cumsum[values[1]])
    sumList.append(oddSum[values[1]-1])
    sumList.append(evenSum[values[1]-1])
    allVals.append(sumList)

for i in range(len(allVals)):
    print(allVals[i][0], " ",allVals[i][1], " ",allVals[i][2], " ",allVals[i][3])
