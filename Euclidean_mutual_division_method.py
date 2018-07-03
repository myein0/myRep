
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
a, b = max(a, b), min(a, b)
if a * b == 0:
    gcd = 0
elif a % b == 0:
    gcd = b
else:
    while a % b != 0: 
        a, b = b, a % b
    gcd = a

print("gcd({}, {}) = {}".format(a_0, b_0, gcd))

