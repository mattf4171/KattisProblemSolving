# The number ð is called the mean of two numbers ð1 and ð2 if ð is equal to (ð1+ð2)/2. Mirkoâs birthday present for Slavko was two integers ð1 and ð2. Slavko promptly calculated their mean which also happened to be an integer but then lost ð2! Help Slavko restore ð2.
#
# Input
# The first and only line of input contains two integers ð1 and ð, both between â1000 and 1000.
#
# Output
# Output ð2 on a single line.
#
nums = [int(x) for x in input().split()]
y = (nums[1] *2) - nums[0]
print(y)
