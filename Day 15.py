'''
modules
-------
-->A modules in python is a file that contains python code such as
-variables
-functions
-classes
-statements

two types of modules
--------------------
user-define
built-in


import Module
print(Module.add(5,6))
print(Modue.sub(6,5))


import math
print(math.sqrt(25))

print(math.factorial(10))
print(math.pow(2,5))


from math import sqrt
print(sqrt(25))

import math as m

print(m.factorial(10))
print(m.pow(2,5))


import os
os.rmdir("Some_Python")



import sys
print(sys.version)
print(sys.exit)
print(sys.path)



import random
print(random.randint(1000,9999))


from collections import Counter, defaultdict
data = ['a','b','c','d']
Counter = Counter(data)
print(Counter)

dd = defaultdict(int)
dd['missing'] +=1
print(dd['missing'])
print(dd)














