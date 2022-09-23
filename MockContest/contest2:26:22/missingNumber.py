numbers = int(input())

strWithMissingNum = list(input())
listOfNums = []
valCheck = 1



def checkneighbor(steps, element, valCheck):
    if steps == 1:
        if element >= len(strWithMissingNum) or strWithMissingNum[element] != str(valCheck):
            print(valCheck)
            return True
        else:
            return False
    elif steps == 2:  
        if element >= len(strWithMissingNum) or strWithMissingNum[element] + strWithMissingNum[element + 1] != str(valCheck):
            print(valCheck)
            return True
        else:
            return False
    else:  # value is 100
        print(valCheck)
        return True

for i in range(numbers):  # (2<=n<=100)
    if i < 9:  # single digit value
        if checkneighbor(1, i, valCheck):
            break

    elif 9 <= i <= 99:  # double digit value
        if checkneighbor(2, i, valCheck):
            break
        strWithMissingNum = strWithMissingNum[:i+1] + strWithMissingNum[i+2:] # more values then remove the leading digit at ith element of string

    else:  # value is 100
        if checkneighbor(3, i, valCheck):
            break
    valCheck += 1

    
