# Input
# The first line of input contains two integers 𝑚 and 𝑛, (1≤𝑚,𝑛≤100). This is followed by 𝑚 lines, each containing 𝑛
# characters. A ‘#’ denotes a black pixel, a ‘.’ denotes a white pixel. For every black pixel, exactly two of its eight
# neighbors are also black.
#
# Output
# Display a single integer representing the number of loops in the input.

# https://open.kattis.com/contests/i6p5t8/problems/amoebas

grid_dimHW = [int(x) for x in input().split(' ')]

DR = [0, 1, 0, -1, 1, -1, -1, 1]
DC = [1, 0, -1, 0, 1, 1, -1, -1]
cnt =0

def dfs(r, c):
    if r< 0 or r >=grid_dimHW[0] or c<0 or c>=grid_dimHW[1]:
        return
    if grid[r][c] == ".":
        return
    grid[r][c] = '.'
    for d in range(8):
        dfs(r+DR[d], c+DC[d]) # recursively check all neighbors that are connected

grid = []
for i in range(grid_dimHW[0]):
    row = [x for x in input()]
    grid.append(row)

for i in range(grid_dimHW[0]):
    for j in range(grid_dimHW[1]):
        if grid[i][j] == "#":
            cnt+=1
            dfs(i,j)
print(cnt)
