# Symmetric_difference: It returns unmatching elements from both sets
# Syn: <First_Set>symmetric_difference(<Second_Set>)
a = {1,2,3,4,5}
b = {'jack',1,5,True,1.5}
c = a.symmetric_difference(b)
print(c)
c = b.symmetric_difference(a)
print(c)