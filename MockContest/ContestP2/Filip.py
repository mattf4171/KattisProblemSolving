values = [int(x) for x in input().split()]
out = max(values)
toShow = 0

while out!=0:
    dig = out%10
    toShow = toShow*10+dig
    out //=10

minOut = min(values)
mintoShow = 0
while minOut!=0:
    digit = minOut%10
    mintoShow = mintoShow*10+digit
    minOut //=10
newVals = [toShow, mintoShow]
print(max(newVals))