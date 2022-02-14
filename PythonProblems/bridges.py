# Author: Matthew Fernandez
# Data: 2/11/22

# Input
# The first line contains two integers, 2≤𝑛≤105, the number of positions, 
# and 𝑛−1≤𝑚≤min(2⋅105,𝑛(𝑛−1)/2), the number of roads. Next come 𝑚 lines, each 
# with 3 numbers 1≤𝑎,𝑏≤𝑛 and 𝑐∈{0,1} which means that there is a road that runs 
# between place 𝑎 and place 𝑏 and contains a single-lane bridge if 𝑐=1, and a 
# double-lane bridge if 𝑐=0. The Westman Islands will always be numbered 1 and 
# Egilsstaðir will always be numbered 𝑛. You can assume that Iceland’s road 
# system is coherent: it is possible to get to every place from every other place. 
# You can also assume that each pair 𝑎,𝑏 appears at most once in the input.

# Output
# Print one line with the smallest number of single-lane bridges that Stefán and 
# Eva have to cross to reach the end of the route.

import math

posRoads = [int(x) for x in input().split()] # read in first vals
singleLaneBridges = [] # list of lists 
smallestDist = 1
for i in range((posRoads[1])): # loop through based on # of roads
    vals = [int(x) for x in input().split()]
    if(vals[2] == 1):
        startEnd = [] # create new list with start and end vals
        startEnd.append(vals[0])
        startEnd.append(vals[1])
        singleLaneBridges.append(startEnd)
for x in singleLaneBridges:
    if(dist() == smallestDist):
        
    
def dist(num1, num2):
    return math.sqrt( (num1**2)+ (num2**2) )