# Modules in Python (library)
# A python containing python statements, variable, functions, classes
# Ready Made Modules
# User- Defined Modules
# import statements are used to call modules

# import math
# help(math)
from math import pow, sqrt, sin


# import os
# help(os)

# power = pow(8,2)
# print(power)
#
# print(sqrt(224))
# print(sin(30))

# volumes of figures

def cuboid(l, w, h):
    return l * w * h

def sphere(r):
    PI = 3.142
    answer = 4/3 * PI * r**3
    return answer

def cylinder(r, h):
    PI = 3.142
    result = PI * (r**2) * h
    return result
