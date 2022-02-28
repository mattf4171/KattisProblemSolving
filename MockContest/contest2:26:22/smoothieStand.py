# Input
# The first line contains two integers 𝑘 and 𝑟, separated by a space. The value 𝑘 is the number of different ingredients Olivia uses in her smoothies and 𝑟 is the number of different recipes she makes. You may assume 1≤𝑘≤100000, 1≤𝑟≤100000, and 1≤𝑘𝑟≤100000. The second line contains 𝑘 integers, which represent the amount of each ingredient she currently has on hand. This is followed by 𝑟 lines, each of which represents a recipe. On each such line, the first 𝑘 space-separated integers represent the amount of each ingredient used in that recipe. This is followed by one integer representing the price charged for one smoothie of that recipe.

# You may assume that all values, except possibly 𝑘 and 𝑟, are nonnegative integers less than or equal to 104. It is guaranteed that each recipe uses at least one ingredient.

# Output
# Output the largest total sales revenue that can be obtained by choosing a single recipe and making as many of that recipe as possible.


k_r = [int(x) for x in input().split()]
availableIngre = [int(x) for x in input().split()]

neededIngre = []

for i in range(k_r[1]):
    temp = [int(x) for x in input().split()]
    neededIngre.append(temp)


# 0(n^2) will cause a time out error!

for i in range(k_r[1]): # rows
    for j in range(k_r[0]): # cols
        if neededIngre[i][j] == 3:
            pass

