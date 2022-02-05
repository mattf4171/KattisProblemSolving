import math

vals = []   # empty lists
base10_vals = []

while(True): # read in the users values
    N = input() # input str type 
    if(len(N) == 0):
        break
    N = float(N) # type cast from str to float
    vals.append(N) # add elements to list
x = 0
for i in range(0, len(vals)):
    # iter = int(vals[i]+1)
    for j in range(2, int(vals[i]+1)):
        x = x + math.log(j) 
    x = math.floor(x) # round down to nearest int
    result = x +1 
    print(result)

# TODO: Fix the odd values for the input as follows
# input:
# 0
# 1
# 3
# 10
# 20
# Output:
# 1
# 1
# 2
# 17
# 59
