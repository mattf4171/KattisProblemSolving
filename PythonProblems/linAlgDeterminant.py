import numpy as np

"""
Matthew Fernandez
1/20/2022

Task

    You are given a square matrix A with dimensions N x N. Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.

Input Format

    The first line contains the integer N.
    The next N lines contains the N space separated elements of array A.

Output Format

    Print the determinant of A.
"""

def determinant(grid):
    print(np.linalg.det(grid).round(1))
    return None

if __name__ == "__main__":
    N = int(input())
    grid = np.array([])
    for _ in range(N):
        n_i = [float(i) for i in input().split(" ")]
        if grid.size == 0:
            grid = np.append(grid, n_i)
        else:
            grid = np.vstack([grid, n_i])
 
    determinant(grid)