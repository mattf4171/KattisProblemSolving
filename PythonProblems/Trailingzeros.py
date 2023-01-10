"""Trailing Zero's in n!
Returns the number of trailing zeroes in n!
"""

def factorial_zeros(n):
    prod = n
    # One time scan to calculate n factorial
    while n > 1:
        prod *= (n - 1)
        n -= 1
    
    cnt = 0
    
    while prod % 10 == 0:
        prod = prod/10
        cnt += 1
    return cnt

if __name__ == "__main__":
    n = int(input()) 
    print(factorial_zeros(n))