######################
# Matthew Fernandez
# Programming contest
######################

'''
Often times it is sufficient to know the rough size of a number, rather than its exact value. For example, a human can reason about which store to visit to buy milk if one store is roughly  kilometer away, and another store is roughly  kilometers away. The exact distance to each store is irrelevant to the decision at hand; only the sizes of the numbers matter.

For this problem, determine the ‘size’ of the factorial of an integer. By size, we mean the number of digits required to represent the answer in base-.

Input
Input consists of up to  integers, one per line. Each is in the range . Input ends at end of file.

Output
For each integer , print the number of digits required to represent  in base-10.
'''

import sys
import math

if __name__ == "__main__":

	# store all possible vaulues in list for easy look up
	# one time calculation
	values = []
	values.append(1)
	values.append(1) # digits needed for inputs: 0 & 1
	digits = 0
	for i in range(2, 1000001):
		# print('Digits: ',digits)
		digits += math.log10(i)
		values.append(math.floor(digits) + 1)
	# print(values[:20])

	input_values = []
	# collect all user input values 
	for i in sys.stdin:
		x = eval(i)
		# x = [eval(j) for j in x] # cast list of str to int
		input_values.append(x)

	# get digit count using pre-defined list of digits required
	for i in range(len(input_values)):
		print(values[ input_values[i] ])
