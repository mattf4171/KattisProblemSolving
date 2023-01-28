import sys
import os

"""
Matthew Fernandez

There are n teams. The number of employees in the ith team is denoted by teamSize[i]. In order to maintain uniformity, 
the team size of at most k teams can be reduced. Find the max number of teams of equal size that can be formed if team size is reduced optimally.


Ex:
    There are n=5 teams, team sizes are teamSize = [1, 2, 2, 3, 4], and the max number of teams whose sie can be reduced, k=2.

    The team size of the last 2 teams can be reduces to 2, thus teamSize = [1, 2, 2, 2, 2]. The max number of teams with equal size is 4.

Fn Description:

    Complete the function equalizeTeamSize in the editor below.

equalizeTeamSize has the following parameters:
 - int teamSize[n]: the number of employees in each team
 - int k: the max number of teams whose size can be reduced

Returns:
 - int: the max number of equal size teams possible

Constraints:
 - 1 <= n <= 2*10^6
 - 1 <= teamSize[i] <= 10^9
 - 0 <= k <= 10^9
"""

def equalizeTeamSize(teamSize, k):
    # binary search method
   
    
    teamSize.sort()
    i, cnt = 0, 0
    j = len(teamSize)-1
    while(j < len(teamSize)):
        if teamSize[j] - teamSize[i] <= k:
            cnt += 1
            i = j + 1
            j = j + len(teamSize)
        else:
            i += 1
            j += 1
    return 0

if __name__ == "__main__":
    n = int(input())
    teamSize = []
    for i in range(n):
        temp = int(input())
        teamSize.append(temp)
    k = int(input())
    maxEqualTeams = equalizeTeamSize(teamSize, k)
    print(maxEqualTeams)


"""
Input:
7       n = 7
1
2
3
4
5
6
7
10      k = 10

Output:
7
"""