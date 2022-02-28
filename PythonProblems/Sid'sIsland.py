import sys
# def 


x_y = [int(x) for x in input().split()]
x = x_y[0]
y = x_y[1]
print(x_y)
matrix = []
for i in range(x):
    line = sys.stdin.readline()
    line = list(line[:-1])
    # rows = [int(x) for x in input()]
    matrix.append(line)

# for i in range(len(matrix)):



print(list(matrix))