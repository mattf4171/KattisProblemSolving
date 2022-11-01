"""

Matthew Fernandez
10/31/2022

Game of Throwns

Daenerys frequently invents games to help teach her second grade Computer Science class about various aspects of the discipline. For this week’s lesson she has the children form a circle and (carefully) throw around a petrified dragon egg.

The  children are numbered from  to  (it is a Computer Science class after all) clockwise around the circle. Child  always starts with the egg. Daenerys will call out one of two things:

a number , indicating that the egg is to be thrown to the child who is  positions clockwise from the current egg holder, wrapping around if necessary. If  is negative, then the throw is to the counter-clockwise direction.

the phrase undo , indicating that the last  throws should be undone. Note that undo commands never undo other undo commands; they just undo commands described in item  above.

For example, if there are  children, and the teacher calls out the four throw commands 8 -2 3 undo 2, the throws will start from child  to child , then from child  to child , then from child  to child . After this, the undo 2 instructions will result in the egg being thrown back from child  to child  and then from child  back to child . If Daenerys calls out  (or , etc.) then the child with the egg simply throws it straight up in the air and (carefully) catches it again.

Daenerys would like a little program that determines where the egg should end up if her commands are executed correctly. Don’t ask what happens to the children if this isn’t the case.

Input
Input consists of two lines. The first line contains two positive integers   (, ) indicating the number of students and how many throw commands Daenerys calls out, respectively. The following line contains the  throw commands. Each command is either an integer  () indicating how many positions to throw the egg clockwise or undo  () indicating that the last  throws should be undone. Daenerys never has the kids undo beyond the start of the game.

Output
Display the number of the child with the egg at the end of the game.

"""


from curses.ascii import isdigit
import sys



if __name__ == "__main__":

    commands = []
    counter = 0
    limit = 0
    for i in sys.stdin:
        if counter == 0:
            x = i.split()
            n = int(x[0])
            k = int(x[1])

        else:
            commands = i.split()

        
        counter += 1
    # print(array)
    # print(len(commands))
    students_tuple = (range(n))
    # wrap_around = 
    completed_command = []
    egg_location = 0
    for i in range(k):
        
        # if the command is a number
        if commands[i].lstrip("-").isdigit():
            if "-" in commands[i]:
                completed_command.append(egg_location)
                egg_location = ( egg_location - int(commands[i].lstrip('-')) ) %(n)
                # print('negative condition: ',egg_location)
            else:
                completed_command.append(egg_location)
                egg_location = ( egg_location + int(commands[i]) ) % (n)
                # print('else ',egg_location )

        else:
            # print("\nprior to undo: ",completed_command)
            egg_location = completed_command[-int(commands[i+1])]
            completed_command = [] # reset 
            # print("undo -> ", egg_location)
            i += 1
        # print(egg_location)
    print(egg_location)