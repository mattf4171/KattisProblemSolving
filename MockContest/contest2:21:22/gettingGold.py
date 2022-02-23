W_H = [int(x) for x in input().split() ]

whole_map = []
for i in range(W_H[1]): # adds each row into whole_map
    map_W = input()
    list_map_W = []
    list_map_W[:] = map_W
    whole_map.append(list_map_W)
# print(len(whole_map)) # have entire map

for i in range(W_H[0]):
    for j in range(W_H[1]):
        if(whole_map[i][j] == "P"):
            start_position = [i,j]

def checkSurroundings(start, next):
    for i in range(end):


# USE OF BFS IS NEEDED

# check positions to the right of startPosition
gold_counter = 0

for i in range(start_position[i],[j][0], W_H[0]): 
    for j in range(start_position[i][j][1], W_H[1]):
        if(i == start_position[0]):
            if(checkSurroundings() ==True): 
                continue
        else:
            break;

# check positions to the left of start Position
for i in range(0,start_position[i],[j][0]):
    for j in range(start_position[i][j][1]):
        if(checkSurroundings() == True):
            continue

