line = [x for x in input().split('-')]
str = ""
for i in range(len(line)):
    str += "".join(line[i])[:1]
print(str)
