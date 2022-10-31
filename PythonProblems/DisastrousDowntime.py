# ######################
# # Matthew Fernandez
# # Programming contest
# ######################
#
# # FIND MAX NUM OF REQUESTS
#
#
# import sys
# import math
#
# if __name__ == "__main__":
#     array = [0 for i in range(1,100001)]
#     # collect all user input values
#     values = []
#     for i in sys.stdin:
#         x = [eval(x) for x in i.split()]
#         values.append(x)
#
#     N = values[0][0]  # upcoming requests
#     K = values[0][1]  # max requests
#     new_values = []
#
#     for i in range(N):
#         new_values.append(values[i+1][0])
#
#     for i in new_values:
#         array[i-1] = int(array[i]) + 1
#         if i+1000 <= 100000:
#             array[i+1000-1] = int(array[i+1000-1]) - 1
#
#     # TODO
#     upperLim = 0
#     x = 0
#     count_vals = []
#     for i in array:
#         if i > 0:
#             x += i
#         elif i < 0:
#             upperLim = x
#             count_vals.append(upperLim)
#             x -= i
#     # (max(count_vals)
#     print(math.ceil(max(count_vals)/K))
#
# ###################################
# # Input
# # 3 2
# # 1000
# # 1010
# # 1999
#
# # Output
# # 2

import sys
import math

if __name__ == '__main__':
    binary_array = [0 for i in range(100000)] # fill zeros with parameter 1 <= N <= 100000
    values = []
    row = 0
    for i in sys.stdin:
        x = i.split()
        if row == 0:
            N = i[0]
            K = i[1]
        if row != 0:
            values.append(x)
        row += 1

    for i in range(N):
        if binary_array[i] > 0:
            x += 1
        elif binary_array[i-1] < 0:

