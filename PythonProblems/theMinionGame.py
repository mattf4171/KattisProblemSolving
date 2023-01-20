"""
Matthew Fernandez
1/19/2022

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
"""

def minion_game(string):
    
    string = string.lower()
    stuart_consonants = ['b','c','d','f','g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 
                        'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    stuart_score = 0
    kevin_score = 0

    # assess stuart's score
    for i in range(len(string)):
        temp = string[i]
        if temp in stuart_consonants: 
            # all combinations of substring starting with index @ i
            stuart_score += len(string) - i

        # assess kevin's score
        else: 
            kevin_score += len(string) - i
    
  
    if stuart_score > kevin_score:
        print("Stuart {}".format(stuart_score))
    elif stuart_score < kevin_score:
        print("Kevin {}".format(kevin_score))
    else:
        print("Draw")

    return

if __name__ == "__main__":
    input_string = input("Input string to play minion game: ")
    minion_game(input_string)