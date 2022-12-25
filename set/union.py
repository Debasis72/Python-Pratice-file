'''
Union: it returns the union of two sets, that means it returns all the values from both sets except
duplicate values.
The same result we can get by using ‘|’ between two sets
Syn: <First_Set>.union(<Second_Set>) or
 <First_Set> | <Second_Set>
'''
a = {1,3,45,1.3}
b = {True,'jack',1,2,3,6,7}
c = a.union(b)
print(c)
c = a|b
print(c)