"""Perfect Number 
- A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
- A divisor of an integer x is an integer that can divide x evenly.
- Given an integer n, return true if n is a perfect number, otherwise, return false.
- https://leetcode.com/problems/perfect-number/
"""

"""Slower Solution O(n)"""

# def perfect_number(num):
#     divisors = []
#     for i in range(1,num):
#         if num%i==0:
#             divisors.append(i)
#     if sum(divisors)==num:
#         return True
#     else:
#         return False
        
"""Better Solution O(sqrt(n))"""

def perfect_number(num):
    
    if num<=1:
        return False
    
    divisors = set([1])
    
    for i in range(2,int(num**0.5)+1):   # from 2 to num**0.5
        if num%i==0:
            divisors.add(i)
            divisors.add(num//i)

    return sum(divisors)==num


if __name__ == "__main__":
    print(perfect_number(4))