# Author: Matthew Fernandez
# Date: 2/10/2022

# Input
# Input consists of up to 1000 test cases, one per line. 
# Each test case is a single positive integer 𝑖≤106. Input ends with a value of zero.

# Output
# For each test case, print out the value of the rightmost (lowest-order) non-zero 
# digit of 𝑖!.

for i in sys.stdin:
    val = i.split()
    if(val == 0): # no more values to read in
        break
    
    # Solve the test case and output the answer