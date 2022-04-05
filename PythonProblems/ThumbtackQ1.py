#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bestPros' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY pros
#  2. INTEGER k
#


def bestPros(pros, k):
    # Write your code here
    dis = [row[0] for row in pros] # distinguish values from 2d array
    rate = [row[1] for row in pros]
    maxDist = max(dis) # max dist value used for alg.
    pms=[]
    # print(rate)
    for i in range(len(dis)):
        score = (maxDist-dis[i])* rate[i] # PMS for each pro
        pms.append(score)
    templist = pms.copy()
    pms_sorted = []   
    # print(pms)
    for j in range(0,k):
        max_score=0
        # sort and give only 1 val per instance of the pms scores
        for i in range(len(templist)):
            if templist[i] > max_score:
                max_score = templist[i]
        pms_sorted.append(max_score)
    bestPros= []
    bestPros_k_less_pros = []
    pcount = 0
    for i in range(0,len(pms_sorted)):
        for x in range(0,len(pms)):
            if pms[x] == pms_sorted[i]:
                if x not in bestPros: # no duplicate instances
                    bestPros.append(x)
                    pcount +=1
                    if pcount == k:
                        break
                if x not in bestPros_k_less_pros: 
                    bestPros_k_less_pros.append(x)
    if len(dis)<k: # fewer suitable pros, than k, rtrn all bestPros
        return bestPros_k_less_pros
                        
    
    return bestPros
p=[
[5,4], 
[4,3], 
[6,5], 
[3,5]
]
k = 2
print(bestPros(p,k))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     pros_rows = int(input().strip())
#     pros_columns = int(input().strip())

#     pros = []

#     for _ in range(pros_rows):
#         pros.append(list(map(int, input().rstrip().split())))
#     k = int(input().strip())
#     result = bestPros(pros, k)
#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')
#     fptr.close()
