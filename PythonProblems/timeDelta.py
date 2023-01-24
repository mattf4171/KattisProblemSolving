import math
import os
import random
import re
import sys

"""
Matthew Fernandez
1/23/2022

When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Input Format

    The first line contains T, the number of testcases.
    Each testcase contains 2 lines, representing time t_1 and time t_2.

Constraints

    Input contains only valid timestamps
    year <= 3000

Output Format

    Print the absolute difference  in seconds.
"""

# Complete the time_delta function below.
def time_delta(t1, t2):
    # returns the abs(t1 - t2)
    
    time_zone = [ int(t1.split()[5]), int(t2.split()[5]) ] # hr-min
    months = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, 
              "Jul":7, "Aug":8, "Sept":9, "Oct":10, "Nov":11, "Dec":12}
    
    x =  int(t1.split()[1]) - int(t2.split()[1])
    day_to_sec = x * (24*3600)
    
    month_to_sec = [ months[t1.split()[2]], months[t2.split()[2]] ] # row 2 - row 1 
    month_to_sec = (month_to_sec[1]-month_to_sec[0]) * 2.628e+6    
    
    year = [int(t1.split()[3]), int(t2.split()[3])]
    year_to_sec = (year[1] - year[0])  * 3.154e+7
    
    diff_hr_to_sec = math.floor(time_zone[0] / 100) * (60**2)
    # condition to update the difference in time
    if time_zone[0] > 999 or time_zone[0] < -999:
        if int(time_zone[0]) < 0:
        # carry the sign
            diff_min_to_sec = -1 * int(str(time_zone[0])[3:]) * 60
        else:
            diff_min_to_sec = int(str(time_zone[0])[2:]) * 60

    elif time_zone[0] > 99 or time_zone[0] < -99:

        if int(time_zone[0]) < 0:
        # carry the sign
            diff_min_to_sec = -1 * int(str(time_zone[0])[2:]) * 60
        else:
            diff_min_to_sec = int(str(time_zone[0])[1:]) * 60
    else:

        if int(time_zone[0]) < 0:
        # carry the sign
            diff_min_to_sec = -1 * int(str(time_zone[0])[1:]) * 60
        else:
            diff_min_to_sec = int(str(time_zone[0])[:]) * 60
    
    time = [t1.split(" ")[4].split(":"), t2.split(" ")[4].split(":")]
    hour_to_sec = ( int(time[0][0]) * (60**2) ) - ( ( int(time[1][0]) * (60**2) ) + diff_hr_to_sec)
    min_to_sec = ( int(time[0][1]) * 60 ) - ( ( int(time[1][1]) * 60) + diff_min_to_sec )
    sec = int(time[0][2]) - int(time[1][2])
    
    return int(abs(hour_to_sec + min_to_sec + sec + day_to_sec + month_to_sec + year_to_sec))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        # fptr.write(delta + '\n')
        print(delta)
    # fptr.close()


"""
Input:
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000


Output:
25200
88200
"""
