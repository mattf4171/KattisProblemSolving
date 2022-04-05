#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 10:33:39 2021

@author: matthewfernandez
Description: You are given two strings, A and B. Return whether A can be 
shifted some number of times to get B.
"""

def is_shifted(a, b):
  # Fill this in.
  temp = ''
  
  if len(a) != len(b):
      return 0
  
  temp = a + a
  
  if(temp.count(b) > 0):
      return 1
  else:
      return 0
  
    
strings = ["DAAC", "ACDA"]
if is_shifted(strings[0], strings[1]):
    print ("Strings are rotations of each other :)")
else: 
    print ('Strings are not rotations of each other :(')