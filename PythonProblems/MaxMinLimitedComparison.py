#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 09:37:32 2021

@author: matthewfernandez
"""

'''
Given a list of nums of size n, where n is greater than 3, find the max and min
of the list using less than 2* (n-1) comparisons. 
'''

def find_min_max(nums):
    # Fill 
    min = nums[0]
    max = nums[1]
    count =0
    for x in nums:
        count += 1
    limit = 2*(count-1)
    print(limit)
print (find_min_max([3,5,1,2,4,8]))