'''
Diffferenece: It returns all elements from first set which are not there in the second set.
Syn: <First_set>.difference(<Secnd_Set>) or
 <First_Set> - <Second_Set>
 '''
a = {1,2,3,4}
b = {1,2,5,6}
c = a.difference(b)
print(c)
c = b.difference(a)
print(c)
c = a-b
print(c)
c = b-a
print(c)