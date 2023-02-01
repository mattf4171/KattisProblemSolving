'''
Matthew Fernandez
2/1/22
Your favorite public transport company LS (we cannot use their real name here, so we permuted the letters) wants to change signs on all bus stops. 
Some bus stops have quite a few buses that stop there and listing all the buses takes space. However, if for example buses 141, 142, 143 
stop there, we can write 141–143 instead and this saves space. Note that just for two buses this does not save space.

You are given a list of buses that stop at a bus stop. What is the shortest representation of this list?

Input
The first line of the input contains one integer N, 1<=N<=1000 the number of buses that stop at a bus stop. Then next line contains a list of N space 
separated integers between 1 and 1000, which denote the bus numbers. All numbers are distinct.

Output
Print the shortest representation of the list of bus numbers. Use the format as in the example, separate numbers with single spaces and output 
them in sorted order.
'''

import sys

if __name__ == "__main__":
    # collect all user input values
    matrix = []
    for i in sys.stdin:
        x = i.split()
        matrix.append(x)

    sorted_busses = [eval(i) for i in matrix[1]]
    sorted_busses.sort()
    # print(sorted_busses)

    counter_arr = []

    for x in range(len(sorted_busses)):
        if x == len(sorted_busses) - 1:
            if sorted_busses[x - 1] + 1 == sorted_busses[x]:
                counter_arr.append(1)
            else:
                counter_arr.append(0)
            break
        if sorted_busses[x] + 1 == sorted_busses[x+1]:
            counter_arr.append(1)
        else:
            counter_arr.append(0)

    ascending = False
    # print(counter_arr)
    counter = 0
    for i in range(len(counter_arr)):
        if i == len(counter_arr)-1:
            print(sorted_busses[i])
            break
        if counter_arr[i] == 1:
            counter += 1
            if counter_arr[i+1] == 1 and not ascending:
                print(sorted_busses[i], end="-")
            elif counter_arr[i+1] == 0 and not ascending:
                print(sorted_busses[i], end=" ")
            ascending = True
        elif counter > 2 and counter_arr[i] == 0:
                print(sorted_busses[i], end=" ")
        else:
            counter = 0
            ascending = False
            print(sorted_busses[i], end=" ")


"""
Input:
6
180 141 174 143 142 175


Output:
141-143 174 175 180

"""