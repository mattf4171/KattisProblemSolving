"""
Matthew Fernandez
Dynamic Programming 
"""

import monk

def monkey_f(self):
    print('monkey_f() is being called')

# replace address of func with monkey_f
monk.A.func = monkey_f
obj = monk.A()

obj.func()