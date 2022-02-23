cipherStr = input()
preKeyStr = input()
cipherTxt = [x for x in cipherStr]
preKey = [y for y in preKeyStr]
key = []
message = []
if(len(preKey) != len(cipherTxt)):
    for i in range(len(preKey)):
        key.append(preKey[i])
    for i in range(len(cipherTxt)-len(preKey)):
        key.append(cipherTxt[i])
else:
    key = preKey
encryption_dict = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8,
                    'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 
                    'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 
                    'Z':25 }
# key_list = list(encryption_dict.keys())
# print(key_list[key_list.index(0)])

# print(list(encryption_dict.values())[list(encryption_dict.keys()).index('A')])
# prints A

# print(cipherTxt)
# print(key)
for i in range(len(key)):
    if(list(encryption_dict.values())[list(encryption_dict.keys()).index(cipherTxt[i])] - list(encryption_dict.values())[list(encryption_dict.keys()).index(key[i])] <0):
        chr = 26 - list(encryption_dict.values())[list(encryption_dict.keys()).index(key[i])] + list(encryption_dict.values())[list(encryption_dict.keys()).index(cipherTxt[i])]
        message.append(list(encryption_dict.keys())[list(encryption_dict.values()).index(chr)])
    else:
        chr = list(encryption_dict.values())[list(encryption_dict.keys()).index(cipherTxt[i])] - list(encryption_dict.values())[list(encryption_dict.keys()).index(key[i])]
        message.append(list(encryption_dict.keys())[list(encryption_dict.values()).index(chr)])
for x in message: print(x)
# list(encryption_dict.values())[list(encryption_dict.keys()).index('A')] # gets the value
# list(encryption_dict.keys())[list(encryption_dict.values()).index(0)] # gets the key