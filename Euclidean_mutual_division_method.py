# coding: UTF-8

import random
N = 100
a = random.randint(0, N)
b = random.randint(0, N)
a_0 = a
b_0 = b

'''
import math
math.gcd(a, b)
'''

if a * b == 0:
    a = 0
else:
    a, b = max(a, b), min(a, b)
    r = a - a // b

    while r != 0:
        r = a % b
        a = b
        b = r

print("gcd({}, {}) = {}".format(a_0, b_0, a))
