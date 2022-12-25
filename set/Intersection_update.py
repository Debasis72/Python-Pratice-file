# Intersection_update: this function will update the First_Set with the result of intersection between
# First_Set and Second_Set.
# Syn: <First_Set>.intersection_update(<Second_Set>)

a = {1,2,3,4,5}
b = {'jack',1,5,True,1.5}
a.intersection_update(b)

print(a)
print(b)
b.intersection_update(a)

print(b)