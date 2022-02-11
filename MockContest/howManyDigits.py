# Author: Matthew Fernandez
# Abstract: 
#   Input
#       Input consists of up to 10000 integers, one per line. 
#       Each is in the range [0,1000000]. Input ends at end of file.
#   Output
#       For each integer 𝑛, print the number of digits required to 
#       represent 𝑛! in base-10.
# Date: 2/4/2022

import math

# constants to access faster than library
pi = 3.14159265358979
e = 2.718281828459045

for i in sys.stdin:
    val = int(i.split())
    if(val[i] ==0): # neg val
        print(0)
        continue
    if(val[i] == 1): # neg val
        print(1)
        continue
    # below operation raises a run time error
    print( math.ceil(math.log(2* pi *val[i] , 10) / 2+val[i]*(math.log(val[i]/e, 10)) ))