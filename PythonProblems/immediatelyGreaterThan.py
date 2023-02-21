"""
Matthew Fernandez
2/21/22

Given an array arr[] of size N containing positive integers and an integer X. 
You need to find the value in the array which is greater than X and closest to it. 
( if no such value exists the answer should be -1)

Input:
  N = 5
  arr[] = {4 67 13 12 15}
  X = 16

Output: 
  67

Explanation: 
  For a given value 16, there is only one value 67 that greater than
  it and so it is the answer.
"""

class Solution:
    # inf has been imported in driver code
    def immediateGreater(self,arr,n,x):
        # if counts == 0 at end of loop, then no immediate greter than value found
        greater_counts = 0
        for i in arr:
            if i > x:
                # condition to check that we have a previous element
                if greater_counts != 0:
                    # if current element is smaller than prev
                    if i < prev:
                        prev = i
                    # Move on to ensure we do not rewrite the prev
                    continue
                # initially ran when the first immediately greater than is found
                greater_counts += 1
                prev = i
        if greater_counts == 0:
            return -1
        else:
            return prev
 

if __name__ == "__main__":
  from math import inf
    tcs = int(input())
    
    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]
        x = int(input())
        
        print(Solution().immediateGreater(arr,n, x))
