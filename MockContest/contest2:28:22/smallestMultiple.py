import sys

# for i in sys.stdin:
for i in range(3):
    # Solve the test case and output the answer
    values = [int(x) for x in input().split()]
    multiple = 1
    for j in range(len(values)): # use bignum to solve this
        multiple = multiple*values[j]
        if j == len(values)-1:
            print(multiple)
