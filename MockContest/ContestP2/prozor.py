# Matthew Fernandez
# 2/18/2022

# Input
# The first line of input contains three integers 𝑅, 𝑆 and 𝐾 (3≤𝐾≤𝑅, 𝑆≤100) that denote 
# the dimensions of Marin’s picture and the length of the side of the racket.

# Each of the following 𝑅 lines contains 𝑆 characters that describe Marin’s picture. The 
# picture’s pixels marked with ‘*’ denote the position of a fly, whereas all the other 
# pixels are marked with ‘.’ and denote empty space. On his window, there is at least 
# one fly that Marin can kill with his racket.

# Output
# The first line of output must contain the maximal number of flies Marin can kill in 
# a single shot.

# The following 𝑅 lines must contain Marin’s picture, on it clearly marked a position 
# of the racket that will ensure Marin kills as many flies as possible. The horizontal 
# sides of the racket are denoted with a series of characters ‘-’ and the vertical ones 
# with ‘|’, whereas angles are denoted with ‘+’. For a more detailed explanation, consult 
# the sample tests.

# Please note: Marin’s racket will affect only the flies located strictly inside the 
# racket, and the racket must be located inside the window with all its parts. In other
# words, it is assumed that the flies located at the sides of the racket will have enough 
# time to fly away.

# R -> height frame, S -> width frame, K -> sides of racket
import sys


firstLine = [int(x) for x in input().split()]
rows = firstLine[0]
cols = firstLine[1]
grid = []
# intRow = []
# runningSumMatrix = []
# runSumRows = []
# for i in range(firstLine[0]): # create the char type matrix from input 
#     rows = [x for x in input().split()]
#     for j in range(0,len(rows)):
#         if(rows[j] == '.'):
#             intRow.append(0)
#         elif(rows[j] == '*'):
#             intRow.append(1)
#     matrix.append(intRow)
# print(matrix)
# def dfs(i, j):
#     return 0


for i in range(firstLine[0]):
    row = sys.stdin.readline()
    print(row)
    for j in range(firstLine[1]):
        if(row[i][j] == "*"):
            grid[i+1][j+1].append(1)
        else:
            grid[i+1][j+1].append(0)
    grid.append(row)
print(grid)
# calc the prefix sum
for i in range(1,rows+1):
    for j in range(1,cols+1):
        grid[i][j] += grid[i][j-1] + grid[i-1][j] - grid[i-1][j-1]

