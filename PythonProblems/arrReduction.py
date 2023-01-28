import time
import math
import sys
import numpy as np

"""
Given an array of n ints, a sequence of n-1 operations must be performed on the array.

In each operation,
- Remove the min and max elements from the current array and add their sum back to the array
- The cost of an operation, cost = ceil( [ (min + max) / (max - min + 1) ] )

Find the total cost to reduce the array to a single element

constraints:
  - 2<= n <= 2*10^5
  - 1 <= arr[i] <= 10^6
  - MUST RUN UNDER 10 sec
"""

"""
parameters: int arr[n]: array to be reduced

"""
def findTotalCost(arr):
    prev = 0
    for i in range(len(arr)-1):
        mini = min(arr)
        maxi = max(arr)
        arr.remove(mini)
        arr.remove(maxi)
        prev += math.ceil( (mini + maxi) / (maxi - mini + 1))
        arr.append(maxi+mini)
    return prev

if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        temp = int(input())
        arr.append(temp)
    startTime = time.time()
    totalCost = findTotalCost(arr)
    executionTime = time.time() - startTime
    print(totalCost)
    print(executionTime)
"""
EX Input:
6
3
5
2
1
9
6

EX Output:
10
"""