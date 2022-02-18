# Matthew Fernandez
# 2/17/22

# Input
# The first line of the input contains two space separated positive integers 𝑁,𝑃 – 
# the total number of commercial breaks in a day and the price of one commercial 
# break. You can assume that 𝑁≤100000 and 𝑃≤1000. On the next line there are 𝑁 
# space-separated integers – the 𝑖’th integer denotes how many students listen to 
# the 𝑖-th commercial break. There are always at most 2000 students listening.

# Output
# Output contains one line with one integer – the biggest expected extra profit Onid 
# can get by selecting a continuous sequence of commercial breaks.


firstRow = [int(x) for x in input().split()]
secondRow = [int(x) for x in input().split()]

numbers = firstRow[0]
cost = firstRow[1]
differences = []
runningSum = []

for i in range(numbers): # differences
    differences.append(secondRow[i]-cost)

for i in range(numbers): # runningSum
    if(i==0):
        runningSum.append(differences[i])
        continue
    if(runningSum[i-1]>=0):
        runningSum.append(runningSum[i-1]+differences[i])
        continue
    runningSum.append(differences[i])

print(max(runningSum))