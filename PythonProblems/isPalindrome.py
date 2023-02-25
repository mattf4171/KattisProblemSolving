"""
Matthew Fernandez
2/24/23

You are given a number n. You need to see if the number is a palindrome or not (recursively)

Input:
n = 101
Output: 1

Input:
n = 100
Output: 0
"""

class Solution:
    def isPalin(self,N):
        #code here
        if N == 0 or N == 1:
            return 1
        return N[0] == N[-1] and isPalin(N[1:-2])

      
 
if __name__ == "__main__":
    tcs = int(input())
    for _ in range(tcs):
      n = int(input())
      print(int(Solution.isPalin(n)))
