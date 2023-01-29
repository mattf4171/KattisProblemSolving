import math

"""
Matthew Fernandez
1/29/22

A prime number is a number which is only divisible by 1 and itself.
Given number N check if it is prime or not.

Expected Time Complexity : O(N^1/2)
Expected Aux Space :  O(1)

 

Constraints:
1 <= N <= 109
"""


class Solution:

    # Time:       O(sqrt(N))
    # Aux space : O(1)
    def isPrime(self, N):
        if N <= 1:
            return False
        if N == 2 or N == 3:
            return True
        if N % 2 == 0 or N % 3 == 0:
            return False
        
        for i in range(5, int(math.sqrt(N)) + 1, 6):
            if N % i == 0 or N % (i + 2) == 0:
                return False
        return True