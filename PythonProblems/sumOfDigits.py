"""
Matthew Fernandez
2/23/23

Input:
n = 99999

Output: 45

Explanation: Sum of digit of 99999 is 45.
"""

class Solution:
    def sumOfDigits(self, n):
        '''
        :param n: given number
        :return: sum of digits of n.
        '''
        return 0 if n == 0 else int(n % 10) + self.sumOfDigits(int(n/10))      
 
if __name__ == "__main__":
  test_cases = int(input())
  for cases in range(test_cases):
    n = int(input())
    print(Solution.sumOfDigits(n))
