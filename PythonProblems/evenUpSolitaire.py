"""
The Even Up Solitaire can be played with a stack of cards each having a numerical value from 1 to 100. The cards are laid out from left to right in a row. At every step, the player is allowed to remove two adjacent cards if the sum of their values is even. The gap is then “closed” by shifting the cards to the right of the gap. The order of the remaining cards is not changed. The game stops when all cards are removed or when no more cards can be removed. The player wins when all cards are removed. If this is not possible, the player should try to minimize the number of cards remaining.

You are given the initial list of cards, in left-to-right order. Determine the minimum number of cards that remain if the player moves optimally.

Input
The input consists of one case. The first line contains an integer  () giving the number of cards to follow. The second line contains  integers indicating the card values from left to right. Each card value is in the range 1 to 100.

Output
Print the minimum number of cards that remain if the player moves optimally.

"""

import sys
from tkinter import E

def min_num_cards_remaining(array):
    """
    Check the adjecent neighbors of array using two stack like objects

    If sum of adj neighbors %2 == 0, we remove the two elements, otherwise remove one element from stack x1

    and leave element in stack x2. 

    Returns: length of stack object x2
    """

    # perform two stacks
    x1 = array
    x2 = []
    i = 0
    while True:
        if len(x1) == 0 :
            print(len(x2))
            return False

        x2.append(x1[0])
        x1.pop(0)
        # print(x1,'  ',x2)

        if (x2[-1] + x1[0]) % 2 == 0:
            x1.pop(0)
            x2.pop(len(x2)-1)
            # print('if -> ',x1,'  ',x2)
        else:
            x2.append(x1[0])
            x1.pop(0)
        # print('x1: ',x1,'\nx2: ',x2, '\ni: ',i)
            

if __name__ == "__main__":

    array = []
    counter = 1

    for i in sys.stdin:
        if counter == 2:
            i = [eval(x) for x in i.split()]
        array.append(i)
        counter += 1

    array = array[1]
    min_num_cards_remaining(array)

