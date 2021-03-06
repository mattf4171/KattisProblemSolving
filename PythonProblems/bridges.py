# Author: Matthew Fernandez
# Data: 2/11/22

# Input
# The first line contains two integers, 2β€πβ€105, the number of positions, 
# and πβ1β€πβ€min(2β105,π(πβ1)/2), the number of roads. Next come π lines, each 
# with 3 numbers 1β€π,πβ€π and πβ{0,1} which means that there is a road that runs 
# between place π and place π and contains a single-lane bridge if π=1, and a 
# double-lane bridge if π=0. The Westman Islands will always be numbered 1 and 
# EgilsstaΓ°ir will always be numbered π. You can assume that Icelandβs road 
# system is coherent: it is possible to get to every place from every other place. 
# You can also assume that each pair π,π appears at most once in the input.

# Output
# Print one line with the smallest number of single-lane bridges that StefΓ‘n and 
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