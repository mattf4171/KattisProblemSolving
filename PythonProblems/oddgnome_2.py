######################
# Matthew Fernandez
# Programming contest
######################

'''
According to the legend of Wizardry and Witchcraft, gnomes live in burrows underground, known as gnome holes. There they dig up and eat the roots of plants, creating little heaps of earth around gardens, causing considerable damage to them.

Mrs. W, very annoyed by the damage, has to regularly de-gnome her garden by throwing the gnomes over the fence. It is a lot of work to throw them one by one because there are so many. Fortunately, the species is so devoted to their kings that each group always follows its king no matter what. In other words, if she were to throw just the king over the fence, all the other gnomes in that group would leave.

So how does Mrs. W identify the king in a group of gnomes? She knows that gnomes travel in a certain order, and the king, being special, is always the only gnome who does not follow that order.

Here are some helpful tips about gnome groups:

There is exactly one king in a group.

Except for the king, gnomes arrange themselves in strictly increasing ID order.

The king is always the only gnome out of that order.

The king is never the first nor the last in the group, because kings like to hide themselves.

Help Mrs. W by finding all the kings!

Input
The input starts with an integer , where , representing the number of gnome groups. Each of the  following lines contains one group of gnomes, starting with an integer , where , representing the number of gnomes in that group. Following on the same line are  space-separated integers, representing the gnome ordering. Within each group all the integers (including the king) are unique and in the range . Excluding the king, each integer is exactly one more than the integer preceding it.

Output
For each group, output the king’s position in the group (where the first gnome in line is number one).
'''

import sys
inputs = []

for i in sys.stdin:
	x = i.split() # each line
	x = [eval(j) for j in x]
	inputs.append(x)

inputs = [x[1:] for x in inputs]   # drop first value
inputs = [x[:-1] for x in inputs]  # drop last element from line 
n = len(inputs)

for i in range(n):
	if i == 0:	# dummy index of inputs 2d matrix
		continue
	row = len(inputs[i])

	for j in range(row):
		if j == row-1:
			continue
		if (inputs[i][j])+1 != inputs[i][j+1]:
			print(j+2)
			break

###################################
# TEST

# 3
# 7 1 2 3 4 8 5 6
# 5 3 4 5 2 6
# 4 10 20 11 12

# EXPECTED
# 5
# 4
# 2