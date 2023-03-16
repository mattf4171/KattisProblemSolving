"""
Matthew Fernandez
2/18/22

Given an unsorted array arr[] of size N. Rotate the array to the left (counter-clockwise direction) by D steps, where D is a positive integer. 

Input:
N = 5, D = 2
arr[] = {1,2,3,4,5}

Output: 3 4 5 1 2

Explanation: 1 2 3 4 5  when rotated
by 2 elements, it becomes 3 4 5 1 2.
"""
import math

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,arr,D,N):
        
        if D==0:
            return arr
        arr.reverse()
        i=0
        j=N-D-1

        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
            
        i=N-D
        j=N-1
        
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1

        return arr
      
      
def main():
    tcs = 1
    
    for _ in range(tcs):
        n = [int(x) for x in input().strip().split()]
        N = n[0]
        D = n[1]
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.rotateArr(arr, D, N)
        
        for i in arr:
          print(i,end=" ")
         
if __name__ == "__main__":
    main()
