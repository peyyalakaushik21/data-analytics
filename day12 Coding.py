'''
Built-in functions
------------------
print()
input()
len()
type()
max()
min()


m = [3,4,1,2]
m.sort()
print(m)


Recursive functions
-------------------
--> A Recursive function that calls itself to solve a problem by breaking it into small or simple sub-problems

def fac(num):
    if num == 1:
        return 1
    return num * fac(num -1)
print(fac(5))


def add(a,b):
    return a+b
res = add(4,5)
print(res)

lambda functions
----------------
-->A lambda function is a small anonamus functions
--> lambda can take n number of arguments, but only one expression

syntax --> lambda arguments : expression


so = lambda a,b,c: a+b+c+a
print(so(3,4,9))



















