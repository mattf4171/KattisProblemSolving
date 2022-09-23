######################
# Matthew Fernandez
# Programming contest
######################

'''
When you compute a large, factorial number, it has a long string of low-order zeros at the end. This makes sense; every time you multiply in something like a  or a , you are sure to pick up another low-order zero. Thus, it’s easy to guess the low-order digit of something like . It’s a little harder to guess what the lowest-order non-zero digit will be. Write a program to do that.

Input
Input consists of up to  test cases, one per line. Each test case is a single positive integer . Input ends with a value of zero.

Output
For each test case, print out the value of the rightmost (lowest-order) non-zero digit of .
'''


import sys
import math
if __name__ == '__main__':
    inputs_2D = []
    for i in sys.stdin:
        x = eval(i)
        inputs_2D.append(x)

    # print(math.log10(3*2) / )
    for i in range(inputs_2D[0][0]):
        

########################################
# TEST

# 3
# 25
# 492
# 0

#EXPECTED
#
# 6
# 4
# 8