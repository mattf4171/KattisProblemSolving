#!/bin/python3

import math
import os
import random
import re
import sys
from typing import final
import numpy as np
import pandas as pd

#
# Complete the 'categorySuggestions' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY categories
#  2. STRING_ARRAY projects
#  3. INTEGER k
#

def categorySuggestions(categories, projects, k):
    # Write your code here
    import numpy as np
    import pandas as pd
    categories_list = []
    manipulatedCatList = []
    list_similarities = []
    projs = np.array(projects)

    for i in range(len(categories)):
        categories_list.append(categories[i].split(',')) # 2D array with 3 columns

    manipulatedCatList = np.asarray(categories_list)
    list_similarities = manipulatedCatList[:,2]
    list_similarities = pd.Series(list_similarities, index=np.arange(0,len(categories_list)))
    list_similarities = list_similarities.sort_values(ascending=False)

    similar_cat = []
    final_suggestions = []
    dummyList = [] #np.array([])
    # print(len(categories))
    for x in range(0,len(projs)):
        for i in range(0,len(categories)):
            if ( categories_list[i][0] == projs[x]):
                similar_cat.append((categories_list[i]))
                # print(categories_list[i]) # sanity check
            elif( categories_list[i][1] == projs[x]):
                similar_cat.append((categories_list[i]))
                # print(categories_list[i]) # sanity check
            else: continue
        # np.append(dummyList, similar_cat)
        dummyList.append(similar_cat)
        # print("\n")
    # sort the list by similarity rating
    similar_cat = sorted(similar_cat,key=lambda l:l[2], reverse=True)
    # print(similar_cat) # works, now need to only output the top k per project
    # print(dummyList) # need to index a 3d list for expected ouput
    
    for i in range(k-2):
        final_suggestions.insert(0, [projs[i]]) # add the project itself to the front of the list
        # print(dummyList[i][:])
        final_suggestions.append(similar_cat[i][:][:])
    
    # condition to stop after the kth array is added to new list to return
    # if len(final_suggestions) >= k:
    #     return final_suggestions
        # if (categories_list[i][])
    return final_suggestions # wrong output, will change


categories = [
    "House Painting,Interior Painting,0.9",
    "Handyman,Massage Therapy,0.1",
    "Handyman,House Painting,0.5",
    "House Painting,House Cleaning,0.6",
    "Furniture Assembly,Handyman,0.8",
    "Furniture Assembly,Massage Therapy,0.1",
    "Plumbing Drain Repair,Junk Removal,0.3"
]
projects = ["House Painting", "Handyman"]
k = 3
# expected output
# categorySuggestions(categories, projects, k) = [
#     ["House Painting", "Interior Painting", "House Cleaning"],
#     ["Handyman", "House Painting", "Interior Painting"] ]
categorySuggestions(categories, projects,k)