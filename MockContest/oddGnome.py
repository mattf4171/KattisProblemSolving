inp = int(input())
output = []
for i in range(inp):
    gnomesList = [int(x) for x in input().split()]
    for x in range(1,len(gnomesList)-1):
        if(gnomesList[x] > gnomesList[x+1]):
            print(x)
            output.append(x)
for i in output:
	print(i)

