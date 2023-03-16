"""
Matthew Fernandez
2/17/2022

Input:
N = 5
arr[] = {4 67 13 12 15}
X = 16

Output: 15

Explanation: For a given value 16, there
are four values which are smaller than
it. But 15 is the number which is smaller
and closest to it with minimum difference
of 1.
"""

class Solution:
    def immediateSmaller(self,arr,n,x):
        #return required ans
        
        #code here
        # base case No value is smaller than x
        
        smaller = -1
        # changed = False
        for i in arr:
            if 0 < x - i < x - smaller:
                smaller = i
        return smaller

if __name__ == "__main__":
    tcs = 1
    
    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]
        x = int(input())
        ob = Solution()
        print(ob.immediateSmaller(arr, n, x))
