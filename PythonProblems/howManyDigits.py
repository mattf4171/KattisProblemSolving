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

# too long
# vals = []   # list to append user input values
# while(True): # read in the users values
#     N = input() # input str type 
#     if(len(N) == 0): # case where line !contain int
#         break
#     N = float(N) # type cast from str to float
#     vals.append(N) # add elements to list

# for i in range(0, len(vals)):
#     x=0 # instantiate to 0 for each loop
#     for j in range(2, int(vals[i]+1)):
#         x = x + math.log(j,10) # log base 10
#     x = math.floor(x) # round down to nearest int
#     result = int(x) + 1 
#     print(result) # show #digits required to show n! for each input