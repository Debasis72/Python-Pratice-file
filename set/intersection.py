'''
Intersection: it returns an intersection elements of two sets, that means it returns only common
elements from both sets.
That same operation we can get by sing ‘&’ operator.
Syn: <First_Set>.intersection(<Second_Set>) or
 <First_Set> & <Second_Set>
'''
a = {1,2,3,4,5}
b = {'jack',1,5,True,1.5}
c = a.intersection(b)
print(c)
c = a&b
print(c)