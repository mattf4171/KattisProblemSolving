"""Trailing Zero's in n!
Returns the number of trailing zeroes in n!
"""

def factorial_zeros(n):
    prod = n
    while n > 1:
        prod *= (n - 1)
        n -= 1
    
    cnt = 0
    for i in str(prod)[::-1]:
        if i == '0':
            cnt +=1
        else:
            break
    return cnt

if __name__ == "__main__":
    n = input() 
    factorial_zeros(n)