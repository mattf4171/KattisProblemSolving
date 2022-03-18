line = str(input())
# compare substrings of 3?
start = 0
end = 3
counter = 0
total = 0
comp_subString = ""
for i in range(len(line)-3):
    # print('*')
    substring = line[start:end]
    for j in range(len(line)-1, -1,-1):
        counter +=1
        print(comp_subString)
        print(substring)
        if counter >3:
            comp_subString = ""
            # break
            j = j+2
        comp_subString = line[j:j-3:-1]
        if comp_subString == substring:
            print(comp_subString)
            print(substring)
            total +=1
        # comp_subString = line[-1:]
        if s

print(total)