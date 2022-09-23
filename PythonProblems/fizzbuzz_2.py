######################
# Matthew Fernandez
# Programming contest
######################

import sys

for i in sys.stdin:
	x_y_n = i.split()
	x_y_n = [eval(i) for i in x_y_n]

x = x_y_n[0]
y = x_y_n[1]
n = x_y_n[-1]

for i in range(1,n+1,1):
	if i%x == 0 and i%y == 0:
		print("FizzBuzz")
	elif i%x == 0:
		print("Fizz")
	elif i%y == 0:
		print("Buzz")
	else:
		print(i)