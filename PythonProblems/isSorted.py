"""
Matthew Fernandez
2/17/2022

isSorted FN: Given an array a[ ] of size N. The task is to check if 
array is sorted or not. A sorted array can either be increasingly sorted 
or decreasingly sorted. Also consider duplicate elements to be sorted.


"""

class Solution:
    def isSorted(self,arr,n):
        # Evaluate the first and last element in list to determine the list order
        a = arr[0]
        if a <= arr[n-1]:
            for i in range(1,n):
                if a <= arr[i]:
                    a = arr[i]
                else:
                    return 0
        else:
            for i in range(1,n):
                if a >= arr[i]:
                    a = arr[i]
                else:
                    return 0
        return 1

if __name__ == "__main__":
    tcs = 1
    
    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]

        print(Solution().isSorted(arr,n))
