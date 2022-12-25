# 1. Creating an empty set using set() and add elements to that empty set.
s = set()
s.add(10)
s.add(20)
s.add('jack')
print(s)

# 2. Creating a set with elements using set().
s = set([1,2,4,'a',2+4j,True]) 
print(s)
print(type(s))

# 3. Creating a set with curly braces.
s = {1,2,3,5,'jack',2.4}
print(s)
print(type(s))