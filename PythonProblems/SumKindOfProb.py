"""
Matthew Fernandez
2/1/22

Sum Kind of Problem

For this problem you will compute various running sums of values for positive integers.

Input
The first line of input contains a single integer P, (1 <= P <= 10,000), which is the number of data sets that follow. 
Each data set should be processed identically and independently. Each data set consists of a single line of input. 
It contains the data set number, K, followed by an integer N, (1 <= N <= 10,000).

Output
For each data set there is one line of output. The single output line consists of the data set number, K, followed by a 
single space followed by three space separated integers S_1, S_2 and S_3 such that:

S_1 = The sum of the first  positive integers.

S_2 = The sum of the first  odd integers.

S_3 = The sum of the first  even integers.

"""

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
