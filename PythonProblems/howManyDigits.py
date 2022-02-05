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

vals = []   # empty lists
base10_vals = []

while(True): # read in the users values
    N = input() # input str type 
    if(len(N) == 0):
        break
    N = float(N) # type cast from str to float
    vals.append(N) # add elements to list
for i in range(0, len(vals)):
    x=0.0 # instantiate to 0 for each loop
    for j in range(2, int(vals[i]+1)):
        x = x + math.log(j,10) 
    x = math.floor(x) # round down to nearest int
    result = int(x) + 1 
    print(result)
