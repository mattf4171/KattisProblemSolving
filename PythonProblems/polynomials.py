import numpy as np

"""
Matthew Fernandez
1/19/2022

You are given the coefficients of a polynomial .
Your task is to find the value of  at point .

Input Format

The first line contains the space separated value of the coefficients in .
The second line contains the value of .

Output Format

Print the desired value.
"""

def polynomial_value(poly, x):
    value = np.polyval(poly, x)
    print(value)
    return None


if __name__ == "__main__":
    poly = input().split(" ")
    poly_floats = []
    for i in poly:
        poly_floats.append(float(i))
    x = int(input())
    polynomial_value(poly_floats, x)