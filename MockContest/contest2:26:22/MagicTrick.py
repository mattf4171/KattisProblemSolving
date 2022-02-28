initial_cards = input()

letters = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t', 'u','v','w','x', 'y', 'z'}
checkedVals = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(len(initial_cards)):
    for j in range(len(letters)):
        if(initial_cards[i] == list(letters)[j]):
            checkedVals[j] +=1

for i in range(len(checkedVals)):
    if(checkedVals[i] >1):
        print(0)
        break
    elif(i == len(checkedVals)-1):
        print(1)
        break
