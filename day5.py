'''
sets
----
--> A set is a collection of unique and unordered elements
--> Duplicate values are not allowed
--> Items are not stored in index order
--> {}

methods
-------
union()
-------
--> it will give to all the values from 2 sets together in once
syntax-->variable_name.intersection(another var)

intersection()
--------------
--> to get different values from both sets
syntax-->variable_name.difference(another var)


remove()
--------
--> used to remove element feom the set. but it through error if element not in set
syntax-->variable_name.remove(element)

discard()
---------
--> used to remove element from the set, but it through error if element not in set
syntax-->variable_name.discard(element)

'''

any = {1,2,2,3,4}
any.remove(2)
print()
