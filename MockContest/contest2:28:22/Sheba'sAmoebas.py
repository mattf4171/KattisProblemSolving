# Input
# The first line of input contains two integers 𝑚 and 𝑛, (1≤𝑚,𝑛≤100). This is followed by 𝑚 lines, each containing 𝑛
# characters. A ‘#’ denotes a black pixel, a ‘.’ denotes a white pixel. For every black pixel, exactly two of its eight
# neighbors are also black.
#
# Output
# Display a single integer representing the number of loops in the input.

# https://open.kattis.com/contests/i6p5t8/problems/amoebas

grid_dimHW = [int(x) for x in input().split(' ')]

DR = [0,1,0,-1]
DC = [1,0,-1,0]
counter = 0

def nearPixel(r, c):
    for dir in range(4):
        r2 = r+DR[dir]
        c2 = c+DC[dir]
        if(r2<0 or r2>=grid_dimHW[0] or c2<0 or c2>=grid_dimHW[1]):
            continue
        if(grid[r2][c2] == "#"):
            return True
    return False;

def dfs(r, c):
    if(r< 0 or r >=grid_dimHW[0] or c<0 or c>=grid_dimHW[1]):
        return 0
    if(grid[r][c] == "."):
        return 0
    g = grid[r][c] == "#" # printing 1 when found?
    grid[r][c] = "."
    # return print(grid[r][c])
    print(grid[r][c])
    if( nearPixel(r,c)):
        # count the nearest BFS values
        return g
    for dir in range(4):
        g += dfs(r+DR[dir], c+DC[dir])
    return g

grid = []
for i in range(grid_dimHW[0]):
    row = [x for x in input()]
    grid.append(row)

for i in range(grid_dimHW[0]):
    for j in range(grid_dimHW[1]):
        print(dfs(i,j))



