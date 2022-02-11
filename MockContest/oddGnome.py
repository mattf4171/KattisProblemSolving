inp = int(input())
output = []
for i in range(inp):
    gnomesList = [int(x) for x in input().split()]
    values = gnomesList[1]
    for x in range(1,len(gnomesList)-1):
        if(gnomesList[x+1] != gnomesList[x]+1):
            output.append(x+1)
            break
for i in output:
	print(i)
